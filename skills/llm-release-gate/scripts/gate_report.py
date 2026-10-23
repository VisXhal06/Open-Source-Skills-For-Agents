#!/usr/bin/env python3
"""LLM release gate report generator.

Reads a local run-manifest.json, computes evidence metrics, and returns a
conservative SHIP / SHIP WITH CONDITIONS / BLOCK verdict.

Standard library only. No network access. Writes only to --out, and only
inside the current workspace.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_TOP = ("change", "claim", "tier", "baseline", "candidate")
VALID_TIERS = {"low", "medium", "high"}

REQUIRED_EVIDENCE: dict[str, list[str]] = {
    "prompt": ["regression_delta", "hard_slice", "cost_delta"],
    "model": [
        "regression_delta",
        "hard_slice",
        "cost_delta",
        "capability_delta",
        "judge_human_agreement",
        "latency_cost",
        "fallback",
    ],
    "retrieval": [
        "regression_delta",
        "hard_slice",
        "cost_delta",
        "recall_at_k",
        "groundedness",
        "index_rollback",
    ],
    "tool_agent": [
        "regression_delta",
        "hard_slice",
        "cost_delta",
        "tool_call_correctness",
        "injection_test",
        "idempotency_retry",
        "step_budget",
    ],
    "infrastructure": [
        "regression_delta",
        "hard_slice",
        "cost_delta",
        "load_test",
        "error_budget",
        "canary_abort",
        "capacity_headroom",
    ],
}

CRITICAL_EVIDENCE: dict[str, set[str]] = {
    "prompt": {"regression_delta", "hard_slice"},
    "model": {"regression_delta", "hard_slice", "fallback"},
    "retrieval": {"regression_delta", "hard_slice", "index_rollback"},
    "tool_agent": {"regression_delta", "hard_slice", "injection_test"},
    "infrastructure": {"regression_delta", "hard_slice", "canary_abort"},
}


class GateError(Exception):
    def __init__(self, message: str, code: int = 3) -> None:
        super().__init__(message)
        self.code = code


def load_manifest(path: str) -> dict[str, Any]:
    try:
        raw = Path(path).read_text(encoding="utf-8-sig")
    except FileNotFoundError as exc:
        raise GateError(f"manifest not found: {path}") from exc
    except OSError as exc:
        raise GateError(f"cannot read manifest: {exc}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise GateError(f"invalid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise GateError("manifest must be a JSON object")
    return data


def validate_manifest(data: dict[str, Any]) -> None:
    missing = [key for key in REQUIRED_TOP if key not in data]
    if missing:
        raise GateError(f"missing top-level keys: {', '.join(missing)}")

    change = data["change"]
    if not isinstance(change, dict):
        raise GateError("change must be an object")
    change_class = change.get("class")
    if change_class not in REQUIRED_EVIDENCE:
        raise GateError(
            "change.class must be one of: " + ", ".join(sorted(REQUIRED_EVIDENCE))
        )
    if not str(change.get("summary", "")).strip():
        raise GateError("change.summary must be a non-empty string")

    if data["tier"] not in VALID_TIERS:
        raise GateError("tier must be one of: low, medium, high")

    if not isinstance(data["claim"], str) or not data["claim"].strip():
        raise GateError("claim must be a non-empty string")

    for run_name in ("baseline", "candidate"):
        run = data[run_name]
        if not isinstance(run, dict):
            raise GateError(f"{run_name} must be an object")
        outcomes(run, run_name)


def outcomes(run: dict[str, Any], name: str = "run") -> list[int]:
    tasks = run.get("tasks") or []
    if tasks:
        if not isinstance(tasks, list):
            raise GateError(f"{name}.tasks must be a list")
        result: list[int] = []
        for task in tasks:
            if not isinstance(task, dict):
                raise GateError(f"{name}.tasks entries must be objects")
            result.append(1 if task.get("passed") is True else 0)
        return result

    if "n" not in run or "passed" not in run:
        raise GateError(f"{name} needs n and passed, or a non-empty tasks list")
    try:
        n = int(run["n"])
        passed = int(run["passed"])
    except (TypeError, ValueError) as exc:
        raise GateError(f"{name}.n and {name}.passed must be integers") from exc
    if n < 1:
        raise GateError(f"{name}.n must be at least 1")
    if passed < 0 or passed > n:
        raise GateError(f"{name}.passed must be between 0 and n")
    return [1] * passed + [0] * (n - passed)


def task_values(run: dict[str, Any], key: str) -> list[float]:
    values: list[float] = []
    for task in run.get("tasks") or []:
        if not isinstance(task, dict):
            continue
        value = task.get(key)
        if isinstance(value, (int, float)):
            values.append(float(value))
    return values


def sum_or_none(values: list[float]) -> float | None:
    return sum(values) if values else None


def percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * (pct / 100.0)
    low = math.floor(rank)
    high = math.ceil(rank)
    if low == high:
        return ordered[int(rank)]
    return ordered[low] * (high - rank) + ordered[high] * (rank - low)


def mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def round_or_none(value: float | None, digits: int = 4) -> float | None:
    return None if value is None else round(value, digits)


def run_metrics(run: dict[str, Any]) -> dict[str, Any]:
    result = outcomes(run)
    n = len(result)
    passed = sum(result)

    tokens = run.get("tokens_total")
    if not isinstance(tokens, (int, float)):
        tokens = sum_or_none(task_values(run, "tokens"))
    cost = run.get("cost_total")
    if not isinstance(cost, (int, float)):
        cost = sum_or_none(task_values(run, "cost"))

    latencies = run.get("latency_ms")
    if not isinstance(latencies, list):
        latencies = task_values(run, "latency_ms")
    latencies = [float(value) for value in latencies if isinstance(value, (int, float))]

    retry_count = run.get("retry_count")
    if not isinstance(retry_count, (int, float)):
        retries = task_values(run, "retries")
        retry_count = sum(retries) if retries else None

    agreement = run.get("judge_human_agreement")
    if not isinstance(agreement, (int, float)):
        pairs = [
            task
            for task in (run.get("tasks") or [])
            if isinstance(task, dict)
            and isinstance(task.get("judge_passed"), bool)
            and isinstance(task.get("passed"), bool)
        ]
        agreement = (
            sum(1 for task in pairs if task["judge_passed"] == task["passed"])
            / len(pairs)
            if pairs
            else None
        )

    return {
        "n": n,
        "passed": passed,
        "pass_rate": round(passed / n, 4) if n else 0.0,
        "tokens_total": round_or_none(float(tokens) if tokens is not None else None, 2),
        "tokens_per_task": round_or_none(
            float(tokens) / n if tokens is not None and n else None, 2
        ),
        "cost_total": round_or_none(float(cost) if cost is not None else None, 4),
        "cost_per_task": round_or_none(
            float(cost) / n if cost is not None and n else None, 4
        ),
        "latency_p50_ms": round_or_none(percentile(latencies, 50), 2),
        "latency_p95_ms": round_or_none(percentile(latencies, 95), 2),
        "retry_rate": round_or_none(
            float(retry_count) / n
            if isinstance(retry_count, (int, float)) and n
            else None,
            4,
        ),
        "judge_human_agreement": round_or_none(
            float(agreement) if isinstance(agreement, (int, float)) else None, 4
        ),
    }


def bootstrap_ci(
    baseline: list[int], candidate: list[int], n_boot: int, seed: int
) -> list[float | None]:
    if len(baseline) < 2 or len(candidate) < 2:
        return [None, None]
    rng = random.Random(seed)
    diffs: list[float] = []
    for _ in range(n_boot):
        b = sum(rng.choice(baseline) for _ in baseline) / len(baseline)
        c = sum(rng.choice(candidate) for _ in candidate) / len(candidate)
        diffs.append(c - b)
    diffs.sort()
    lo = diffs[int(0.025 * (len(diffs) - 1))]
    hi = diffs[int(0.975 * (len(diffs) - 1))]
    return [round(lo * 100, 2), round(hi * 100, 2)]


def slice_metrics(run: dict[str, Any]) -> dict[str, dict[str, Any]]:
    groups: dict[str, list[int]] = {}
    for task in run.get("tasks") or []:
        if not isinstance(task, dict):
            continue
        label = str(task.get("slice") or "all")
        groups.setdefault(label, []).append(1 if task.get("passed") is True else 0)
    return {
        label: {
            "n": len(values),
            "pass_rate": round(sum(values) / len(values), 4),
        }
        for label, values in sorted(groups.items())
    }


def combine_slices(
    baseline: dict[str, dict[str, Any]], candidate: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for label in sorted(set(baseline) | set(candidate)):
        before = baseline.get(label)
        after = candidate.get(label)
        delta = None
        if before and after:
            delta = round((after["pass_rate"] - before["pass_rate"]) * 100, 2)
        rows.append(
            {
                "slice": label,
                "baseline_n": before["n"] if before else 0,
                "candidate_n": after["n"] if after else 0,
                "baseline_pass_rate": before["pass_rate"] if before else None,
                "candidate_pass_rate": after["pass_rate"] if after else None,
                "delta_pp": delta,
            }
        )
    return rows


def evidence_status(
    data: dict[str, Any], change_class: str
) -> tuple[dict[str, str], list[str], list[str], list[str]]:
    entries = data.get("evidence") or []
    if not isinstance(entries, list):
        raise GateError("evidence must be a list")
    statuses: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id"):
            raise GateError("each evidence entry needs an id")
        statuses[str(entry["id"])] = str(entry.get("status") or "missing").lower()

    required = REQUIRED_EVIDENCE[change_class]
    present = [item for item in required if statuses.get(item) == "present"]
    waived = [item for item in required if statuses.get(item) == "waived"]
    missing = [
        item
        for item in required
        if statuses.get(item) not in {"present", "waived"}
    ]
    return statuses, present, missing, waived


def evidence_owner(data: dict[str, Any], evidence_id: str) -> str:
    for entry in data.get("evidence") or []:
        if isinstance(entry, dict) and entry.get("id") == evidence_id:
            return str(entry.get("owner") or "unassigned")
    return "unassigned"


def budget_checks(
    data: dict[str, Any],
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    delta_pp: float,
) -> list[dict[str, Any]]:
    budgets = data.get("budgets") or {}
    if not isinstance(budgets, dict):
        raise GateError("budgets must be an object")
    checks: list[dict[str, Any]] = []

    def add(
        name: str,
        before: Any,
        after: Any,
        limit: Any,
        status: str,
        note: str = "",
    ) -> None:
        checks.append(
            {
                "metric": name,
                "before": before,
                "after": after,
                "limit": limit,
                "status": status,
                "note": note,
            }
        )

    pass_min = budgets.get("pass_rate_min")
    if isinstance(pass_min, (int, float)):
        status = "pass" if candidate["pass_rate"] >= float(pass_min) else "fail"
        add("pass_rate", baseline["pass_rate"], candidate["pass_rate"], pass_min, status)

    cost_max = budgets.get("cost_per_task_max")
    if isinstance(cost_max, (int, float)) and candidate["cost_per_task"] is not None:
        status = "pass" if candidate["cost_per_task"] <= float(cost_max) else "fail"
        add(
            "cost_per_task",
            baseline["cost_per_task"],
            candidate["cost_per_task"],
            cost_max,
            status,
        )

    latency_max = budgets.get("latency_p95_ms_max")
    if isinstance(latency_max, (int, float)) and candidate["latency_p95_ms"] is not None:
        status = (
            "pass" if candidate["latency_p95_ms"] <= float(latency_max) else "fail"
        )
        add(
            "latency_p95_ms",
            baseline["latency_p95_ms"],
            candidate["latency_p95_ms"],
            latency_max,
            status,
        )

    token_max = budgets.get("tokens_per_task_max")
    if isinstance(token_max, (int, float)) and candidate["tokens_per_task"] is not None:
        status = (
            "pass" if candidate["tokens_per_task"] <= float(token_max) else "fail"
        )
        add(
            "tokens_per_task",
            baseline["tokens_per_task"],
            candidate["tokens_per_task"],
            token_max,
            status,
        )

    retry_max = budgets.get("retry_rate_max")
    if isinstance(retry_max, (int, float)) and candidate["retry_rate"] is not None:
        status = "pass" if candidate["retry_rate"] <= float(retry_max) else "fail"
        add("retry_rate", baseline["retry_rate"], candidate["retry_rate"], retry_max, status)

    floor = budgets.get("regression_floor_pp", 0.0)
    if isinstance(floor, (int, float)):
        floor = abs(float(floor))
        if delta_pp < -floor:
            status = "fail"
        elif delta_pp < 0:
            status = "watch"
        else:
            status = "pass"
        limit = 0.0 if floor == 0 else -floor
        add("regression_delta_pp", 0.0, round(delta_pp, 2), limit, status)

    return checks


def add_condition(
    conditions: list[dict[str, str]],
    text: str,
    owner: str = "unassigned",
    next_action: str = "",
    signal: str = "",
    expiry: str = "",
) -> None:
    conditions.append(
        {
            "condition": text,
            "owner": owner,
            "expiry": expiry or "set before release",
            "signal": signal or "set before release",
            "next_action": next_action or text,
        }
    )


def add_blocker(
    blockers: list[dict[str, str]], text: str, next_action: str
) -> None:
    blockers.append({"blocker": text, "next_action": next_action})


def build_report(data: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    change = data["change"]
    change_class = str(change["class"])
    tier = str(data["tier"])
    claim = str(data["claim"]).strip()
    required = REQUIRED_EVIDENCE[change_class]

    baseline = run_metrics(data["baseline"])
    candidate = run_metrics(data["candidate"])
    baseline_outcomes = outcomes(data["baseline"], "baseline")
    candidate_outcomes = outcomes(data["candidate"], "candidate")

    delta_pp = round((candidate["pass_rate"] - baseline["pass_rate"]) * 100, 2)
    ci = bootstrap_ci(baseline_outcomes, candidate_outcomes, args.bootstrap, args.seed)
    baseline_slices = slice_metrics(data["baseline"])
    candidate_slices = slice_metrics(data["candidate"])
    slices = combine_slices(baseline_slices, candidate_slices)
    budgets = budget_checks(data, baseline, candidate, delta_pp)

    statuses, present, missing, waived = evidence_status(data, change_class)
    blockers: list[dict[str, str]] = []
    conditions: list[dict[str, str]] = []

    for evidence_id in required:
        status = statuses.get(evidence_id, "missing")
        owner = evidence_owner(data, evidence_id)
        critical = evidence_id in CRITICAL_EVIDENCE[change_class]
        if status == "present":
            continue
        if status == "waived":
            if tier == "high" or (tier == "medium" and critical):
                add_blocker(
                    blockers,
                    f"Critical evidence is waived on a {tier}-tier change: {evidence_id}",
                    f"Replace the waiver with evidence or downgrade the change with a named owner.",
                )
            else:
                add_condition(
                    conditions,
                    f"Evidence waived: {evidence_id}",
                    owner=owner,
                    next_action=f"Provide {evidence_id} or record an accepted risk.",
                    signal=f"Track the gap for {evidence_id}.",
                )
            continue

        if tier == "high" or (tier == "medium" and critical):
            add_blocker(
                blockers,
                f"Missing required evidence: {evidence_id}",
                f"Add {evidence_id} and rerun the gate.",
            )
        else:
            add_condition(
                conditions,
                f"Missing evidence: {evidence_id}",
                owner=owner,
                next_action=f"Add {evidence_id} and rerun the gate.",
                signal=f"Monitor the risk covered by {evidence_id}.",
            )

    if len(claim) < 20:
        if tier in {"medium", "high"}:
            add_blocker(
                blockers,
                "Claim is too short to be falsifiable.",
                "Write one sentence naming the target slice and the guardrail.",
            )
        else:
            add_condition(
                conditions,
                "Claim is too short to be falsifiable.",
                next_action="Write one sentence naming the target slice and the guardrail.",
            )
    elif not any(
        phrase in claim.lower()
        for phrase in ("without", "no regress", "guardrail", "must not")
    ):
        add_condition(
            conditions,
            "Claim does not name a guardrail.",
            next_action="State what must not regress.",
            signal="Re-check the guardrail after rollout.",
        )

    if baseline["n"] < 20 or candidate["n"] < 20:
        text = (
            f"Underpowered evidence: baseline n={baseline['n']}, "
            f"candidate n={candidate['n']} (minimum 20 paired tasks)."
        )
        if tier == "high":
            add_blocker(blockers, text, "Add paired tasks until n >= 20 and rerun.")
        else:
            add_condition(
                conditions,
                text,
                next_action="Add paired tasks and label the current result directional.",
                signal="Track the next eval batch.",
            )

    if delta_pp < 0:
        if ci[0] is not None and ci[0] < 0:
            add_blocker(
                blockers,
                f"Regression: pass rate delta {delta_pp}pp, 95% CI {ci}.",
                "Fix the regression or provide a slice-level justification.",
            )
        else:
            add_condition(
                conditions,
                f"Negative delta {delta_pp}pp with a CI crossing zero; result is directional.",
                next_action="Increase sample size and rerun before claiming improvement.",
                signal="Monitor the regression set.",
            )
    elif ci[0] is not None and ci[0] <= 0 <= ci[1]:
        text = f"Pass-rate CI crosses zero: delta {delta_pp}pp, 95% CI {ci}."
        if tier == "high":
            add_blocker(
                blockers,
                text,
                "Increase paired sample size until the CI excludes zero.",
            )
        else:
            add_condition(
                conditions,
                text,
                next_action="Treat the gain as directional and rerun with more paired tasks.",
                signal="Monitor the regression set and the hard slice.",
            )

    for check in budgets:
        if check["status"] == "fail":
            if tier == "high":
                add_blocker(
                    blockers,
                    f"Budget breached: {check['metric']} after={check['after']} limit={check['limit']}",
                    "Bring the metric inside budget or choose a different change.",
                )
            else:
                add_condition(
                    conditions,
                    f"Budget breached: {check['metric']} after={check['after']} limit={check['limit']}",
                    owner="release-owner",
                    next_action="Set a cost or latency mitigation with a named owner.",
                    signal=f"Alert on {check['metric']}.",
                )
        elif check["status"] == "watch":
            add_condition(
                conditions,
                f"Budget watch: {check['metric']} after={check['after']} limit={check['limit']}",
                owner="release-owner",
                next_action="Confirm the delta is acceptable and monitor it.",
                signal=f"Alert on {check['metric']}.",
            )

    risks = data.get("risks") or []
    if not isinstance(risks, list):
        raise GateError("risks must be a list")
    open_high = [
        risk
        for risk in risks
        if isinstance(risk, dict)
        and str(risk.get("severity", "")).lower() == "high"
        and str(risk.get("status", "open")).lower() not in {"closed", "mitigated"}
    ]
    for risk in open_high:
        add_blocker(
            blockers,
            f"Open high-severity risk: {risk.get('name', 'unnamed risk')}",
            str(risk.get("mitigation") or "Mitigate the risk or record an accepted risk."),
        )

    rollback = data.get("rollback") or {}
    if not isinstance(rollback, dict):
        raise GateError("rollback must be an object")
    rollback_steps = rollback.get("steps") or []
    rollback_owner = rollback.get("owner")
    rollback_tested = bool(rollback.get("tested", False))
    if not rollback_steps or not rollback_owner:
        add_blocker(
            blockers,
            "Rollback is missing steps or an owner.",
            "Write executable rollback steps and name an owner.",
        )
    elif not rollback_tested:
        if tier == "high":
            add_blocker(
                blockers,
                "High-tier rollback is not tested.",
                "Test the rollback and record the result.",
            )
        else:
            add_condition(
                conditions,
                "Rollback is not tested.",
                owner=str(rollback_owner),
                next_action="Run the rollback in staging and record the result.",
                signal="Rollback drill result before release.",
            )

    observability = data.get("observability") or {}
    if not isinstance(observability, dict):
        raise GateError("observability must be an object")
    if tier in {"medium", "high"}:
        if not observability.get("trace_fields"):
            text = "No trace fields are defined; a bad answer cannot be reconstructed."
            if tier == "high":
                add_blocker(blockers, text, "Add prompt/model/retrieval/tool trace fields.")
            else:
                add_condition(
                    conditions,
                    text,
                    next_action="Add prompt/model/retrieval/tool trace fields.",
                    signal="Trace completeness check.",
                )
        if not observability.get("alerts"):
            text = "No alert thresholds are defined for the release."
            if tier == "high":
                add_blocker(blockers, text, "Add quality, latency, and cost alerts.")
            else:
                add_condition(
                    conditions,
                    text,
                    next_action="Add quality, latency, and cost alerts.",
                    signal="Alert configuration review.",
                )

    if tier == "high" and conditions:
        add_blocker(
            blockers,
            "High-tier change has open conditions; high tier cannot ship with conditions.",
            "Close every condition or justify a lower tier.",
        )

    if blockers:
        verdict = "BLOCK"
    elif conditions:
        verdict = "SHIP WITH CONDITIONS"
    else:
        verdict = "SHIP"

    report: dict[str, Any] = {
        "skill": "llm-release-gate",
        "skill_version": "0.1.0",
        "change": change,
        "claim": claim,
        "tier": tier,
        "verdict": verdict,
        "conditions": conditions,
        "blockers": blockers,
        "metrics": {
            "baseline": baseline,
            "candidate": candidate,
            "pass_rate_delta_pp": delta_pp,
            "pass_rate_delta_ci95": ci,
            "slices": slices,
        },
        "budgets": budgets,
        "evidence": {
            "required": required,
            "present": present,
            "missing": missing,
            "waived": waived,
            "statuses": statuses,
        },
        "risks": {
            "total": len(risks),
            "open_high": len(open_high),
        },
        "rollback": {
            "steps": len(rollback_steps) if isinstance(rollback_steps, list) else 0,
            "owner": rollback_owner,
            "tested": rollback_tested,
            "executable": bool(rollback_steps and rollback_owner),
        },
        "observability": observability,
        "what_was_not_verified": [
            item for item in missing + waived if item not in present
        ],
    }
    if not args.no_timestamp:
        report["generated_at"] = datetime.now(timezone.utc).isoformat()
    return report


def fmt(value: Any) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.4f}".rstrip("0").rstrip(".")
    return str(value)


def render_markdown(report: dict[str, Any]) -> str:
    change = report["change"]
    metrics = report["metrics"]
    before = metrics["baseline"]
    after = metrics["candidate"]
    lines: list[str] = []
    lines.append(f"# LLM Release Gate — {change.get('summary', 'change')}")
    lines.append("")
    lines.append(f"**Verdict: {report['verdict']}**")
    lines.append("")
    lines.append(f"**Change class:** `{change.get('class')}`  ")
    lines.append(f"**Tier:** `{report['tier']}`  ")
    lines.append(f"**Claim:** {report['claim']}")
    lines.append("")
    lines.append("## Evidence")
    lines.append("")
    lines.append("| ID | Status |")
    lines.append("| --- | --- |")
    for item in report["evidence"]["required"]:
        status = report["evidence"]["statuses"].get(item, "missing")
        lines.append(f"| `{item}` | {status} |")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    lines.append("| Metric | Baseline | Candidate | Delta |")
    lines.append("| --- | ---: | ---: | ---: |")
    lines.append(
        f"| Pass rate | {fmt(before['pass_rate'])} | {fmt(after['pass_rate'])} | {fmt(metrics['pass_rate_delta_pp'])}pp |"
    )
    lines.append(
        f"| Pass-rate 95% CI | — | — | {fmt(metrics['pass_rate_delta_ci95'][0])} to {fmt(metrics['pass_rate_delta_ci95'][1])}pp |"
    )
    lines.append(
        f"| Tokens / task | {fmt(before['tokens_per_task'])} | {fmt(after['tokens_per_task'])} | — |"
    )
    lines.append(
        f"| Cost / task | {fmt(before['cost_per_task'])} | {fmt(after['cost_per_task'])} | — |"
    )
    lines.append(
        f"| Latency p95 (ms) | {fmt(before['latency_p95_ms'])} | {fmt(after['latency_p95_ms'])} | — |"
    )
    lines.append(
        f"| Retry rate | {fmt(before['retry_rate'])} | {fmt(after['retry_rate'])} | — |"
    )
    lines.append("")
    if metrics["slices"]:
        lines.append("## Slices")
        lines.append("")
        lines.append("| Slice | Baseline n | Candidate n | Baseline | Candidate | Delta |")
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
        for row in metrics["slices"]:
            lines.append(
                f"| {row['slice']} | {row['baseline_n']} | {row['candidate_n']} | "
                f"{fmt(row['baseline_pass_rate'])} | {fmt(row['candidate_pass_rate'])} | "
                f"{fmt(row['delta_pp'])}pp |"
            )
        lines.append("")
    lines.append("## Budgets")
    lines.append("")
    if report["budgets"]:
        lines.append("| Metric | Before | After | Limit | Status |")
        lines.append("| --- | ---: | ---: | ---: | --- |")
        for check in report["budgets"]:
            lines.append(
                f"| {check['metric']} | {fmt(check['before'])} | {fmt(check['after'])} | "
                f"{fmt(check['limit'])} | {check['status']} |"
            )
    else:
        lines.append("No budgets were provided. That is a finding, not a pass.")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    if report["conditions"]:
        for item in report["conditions"]:
            lines.append(
                f"- **{item['condition']}** — owner: {item['owner']}; "
                f"expiry: {item['expiry']}; signal: {item['signal']}; "
                f"next: {item['next_action']}"
            )
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Blockers")
    lines.append("")
    if report["blockers"]:
        for item in report["blockers"]:
            lines.append(f"- **{item['blocker']}** — next: {item['next_action']}")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Observability and rollback")
    lines.append("")
    lines.append(f"- Trace fields: {report['observability'].get('trace_fields', [])}")
    lines.append(f"- Alerts: {report['observability'].get('alerts', [])}")
    lines.append(
        f"- Rollback steps: {report['rollback']['steps']}; "
        f"owner: {report['rollback']['owner']}; tested: {report['rollback']['tested']}"
    )
    lines.append("")
    lines.append("## What was not verified")
    lines.append("")
    if report["what_was_not_verified"]:
        for item in report["what_was_not_verified"]:
            lines.append(f"- {item}")
    else:
        lines.append("No required rows were missing or waived.")
    lines.append("")
    lines.append("## Next action")
    lines.append("")
    if report["blockers"]:
        lines.append(report["blockers"][0]["next_action"])
    elif report["conditions"]:
        lines.append(report["conditions"][0]["next_action"])
    else:
        lines.append("Ship with the rollback plan ready and monitor the named signals.")
    if "generated_at" in report:
        lines.append("")
        lines.append(f"_Generated: {report['generated_at']}_")
    lines.append("")
    return "\n".join(lines)


def ensure_out_path(out: str) -> Path:
    root = Path.cwd().resolve()
    path = Path(out).resolve()
    if not path.is_relative_to(root):
        raise GateError("--out must be inside the current workspace", 3)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute an LLM release verdict from a local run manifest."
    )
    parser.add_argument("--manifest", required=True, help="path to run-manifest.json")
    parser.add_argument(
        "--format",
        choices=("json", "md"),
        default="json",
        help="output format (default: json)",
    )
    parser.add_argument("--out", help="write to this path inside the workspace")
    parser.add_argument(
        "--bootstrap",
        type=int,
        default=2000,
        help="bootstrap resamples for the pass-rate CI (default: 2000)",
    )
    parser.add_argument("--seed", type=int, default=42, help="bootstrap seed")
    parser.add_argument(
        "--no-timestamp",
        action="store_true",
        help="omit generated_at for deterministic diffing",
    )
    args = parser.parse_args()
    if args.bootstrap < 100:
        parser.error("--bootstrap must be at least 100")
    return args


def main() -> int:
    args = parse_args()
    try:
        data = load_manifest(args.manifest)
        validate_manifest(data)
        report = build_report(data, args)
        if args.format == "md":
            text = render_markdown(report)
        else:
            text = json.dumps(report, indent=2, sort_keys=True)

        if args.out:
            path = ensure_out_path(args.out)
            path.write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")
        else:
            print(text)

        return 2 if report["evidence"]["missing"] or report["evidence"]["waived"] else 0
    except GateError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.code
    except (OSError, ValueError, TypeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
