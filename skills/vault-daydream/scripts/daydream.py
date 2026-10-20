#!/usr/bin/env python3
"""Vault Daydream helper.

Deterministic half of the Vault Daydream skill: resolve an Obsidian vault,
scan recent notes, sample recency-weighted pairs, and save accepted insights.

Stdlib only. Works on Windows, macOS, and Linux (Python 3.8+).

Subcommands:
    resolve   Find and report the vault root (optionally save it).
    scan      Scan recent markdown notes and write a scan JSON.
    sample    Build recency-weighted, history-aware note pairs.
    batch     Print one batch of pairs in a compact, agent-readable form.
    save      Write insight notes, digest, daily note, and history.
    stats     Show daydream history for a vault.
"""

import argparse
import json
import os
import random
import re
import sys
import tempfile
import unicodedata
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

EXCLUDE_DIRS = {
    ".obsidian",
    ".git",
    ".trash",
    ".claude",
    ".agents",
    "node_modules",
    "templates",
    "daydreams",
    "ai-research",
}

LOOKBACK_DAYS = 120
MAX_NOTES = 200
PAIR_COUNT = 30
MAX_EXCERPT_WORDS = 500
SCORE_THRESHOLD = 7.0
HISTORY_REL = Path("ai-research") / "daydream" / "history.json"
DAYDREAMS_REL = Path("Daydreams")
DIGESTS_REL = Path("Daydreams") / "digests"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# --------------------------------------------------------------------------
# Small utilities
# --------------------------------------------------------------------------


def eprint(*args):
    print(*args, file=sys.stderr)


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        eprint(f"WARN: could not read {path}: {exc}")
        return ""


def write_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def write_json(path, data):
    write_text(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def read_json(path):
    with Path(path).open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def config_path():
    base = os.environ.get("XDG_CONFIG_HOME")
    root = Path(base) if base else Path.home() / ".config"
    return root / "vault-daydream" / "config.json"


def load_config():
    path = config_path()
    if not path.exists():
        return {}
    try:
        data = read_json(path)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        eprint(f"WARN: ignoring unreadable config {path}")
        return {}


def save_config(data):
    path = config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(path, data)
    return path


def default_workfile(name, today):
    root = Path(tempfile.gettempdir()) / "vault-daydream"
    root.mkdir(parents=True, exist_ok=True)
    return root / f"{name}-{today}.json"


def slugify(value, fallback="daydream", limit=50):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    if not value:
        value = fallback
    value = value[:limit].rstrip("-")
    reserved = {
        "con", "prn", "aux", "nul",
        *(f"com{i}" for i in range(1, 10)),
        *(f"lpt{i}" for i in range(1, 10)),
    }
    if value.lower() in reserved:
        value = f"note-{value}"
    return value


def yaml_string(value):
    text = str(value if value is not None else "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    text = text.replace("\r", " ").replace("\n", " ")
    return f'"{text}"'


def iso_date(now=None):
    return (now or datetime.now()).strftime("%Y-%m-%d")


def compact_date(now=None):
    return (now or datetime.now()).strftime("%Y%m%d")


def parse_date(value):
    for fmt in ("%Y%m%d", "%Y-%m-%d", "%Y_%m_%d"):
        try:
            return datetime.strptime(str(value), fmt)
        except ValueError:
            pass
    return None


# --------------------------------------------------------------------------
# Vault discovery
# --------------------------------------------------------------------------


def is_vault(path):
    return (Path(path) / ".obsidian").is_dir()


def walk_up_for_vault(start):
    current = Path(start).resolve()
    for candidate in [current, *current.parents]:
        if is_vault(candidate):
            return candidate
    return None


def scan_common_locations():
    home = Path.home()
    roots = [
        home,
        home / "Documents",
        home / "Desktop",
        home / "Notes",
        home / "Obsidian",
        home / "vaults",
        home / "Vaults",
        home / "iCloudDrive",
    ]
    skip = EXCLUDE_DIRS | {
        "appdata",
        "application data",
        "library",
        "downloads",
        "venv",
        "__pycache__",
        "dist",
        "build",
        "site-packages",
    }
    seen = set()
    visited = 0
    for root in roots:
        if not root.is_dir():
            continue
        root = root.resolve()
        if root in seen:
            continue
        seen.add(root)
        if is_vault(root):
            return root
        for dirpath, dirnames, _filenames in os.walk(root):
            visited += 1
            if visited > 4000:
                return None
            rel = Path(dirpath).relative_to(root)
            if len(rel.parts) >= 3:
                dirnames[:] = []
                continue
            dirnames[:] = [
                d for d in dirnames
                if not d.startswith(".") and d.lower() not in skip
            ]
            candidate = Path(dirpath)
            if ".obsidian" in dirnames:
                return candidate
    return None


def find_vault(explicit=None):
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if not path.is_dir():
            raise SystemExit(f"Vault path is not a directory: {path}")
        return path

    env_value = os.environ.get("DAYDREAM_VAULT")
    if env_value:
        path = Path(env_value).expanduser().resolve()
        if path.is_dir():
            return path
        eprint(f"WARN: DAYDREAM_VAULT is not a directory: {path}")

    configured = load_config().get("vault")
    if configured:
        path = Path(configured).expanduser()
        if path.is_dir():
            return path.resolve()
        eprint(f"WARN: configured vault is missing: {path}")

    found = walk_up_for_vault(Path.cwd())
    if found:
        return found

    found = scan_common_locations()
    if found:
        return found.resolve()

    raise SystemExit(
        "No Obsidian vault found.\n"
        "Fix this in one of three ways:\n"
        "  1. Run from inside the vault.\n"
        "  2. Set DAYDREAM_VAULT=/path/to/vault\n"
        "  3. Run: python scripts/daydream.py resolve --set /path/to/vault"
    )


# --------------------------------------------------------------------------
# Note cleaning and scanning
# --------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A\ufeff?\s*---\r?\n.*?\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
WIKILINK_RE = re.compile(r"!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
MDLINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]+\)")
URL_RE = re.compile(r"https?://\S+")
HTML_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"(?m)^#{1,6}[ \t]*")
LIST_RE = re.compile(r"(?m)^\s*(?:[-*+]\s+|\d+\.\s+|>\s*)")
HEADING_TITLE_RE = re.compile(r"(?m)^#\s+(.+?)\s*$")


def clean_note(text):
    text = text.lstrip("\ufeff")
    text = FRONTMATTER_RE.sub("", text)
    text = FENCE_RE.sub(" ", text)
    text = WIKILINK_RE.sub(lambda m: (m.group(2) or m.group(1)).split("#")[0], text)
    text = MDLINK_RE.sub(lambda m: m.group(1), text)
    text = URL_RE.sub(" ", text)
    text = HTML_RE.sub(" ", text)
    text = HEADING_RE.sub("", text)
    text = LIST_RE.sub("", text)
    text = text.replace("`", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_title(text, fallback):
    text = text.lstrip("\ufeff")
    text = FRONTMATTER_RE.sub("", text)
    match = HEADING_TITLE_RE.search(text)
    if not match:
        return fallback
    title = clean_note(match.group(1)).strip()
    return title or fallback


def scan_notes(vault, days=LOOKBACK_DAYS, max_notes=MAX_NOTES, words=MAX_EXCERPT_WORDS):
    now = datetime.now()
    cutoff = now.timestamp() - days * 86400
    found = []

    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = sorted(
            d for d in dirnames
            if not d.startswith(".") and d.lower() not in EXCLUDE_DIRS
        )
        for name in filenames:
            if not name.lower().endswith(".md") or name.startswith("."):
                continue
            path = Path(dirpath) / name
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            if mtime < cutoff:
                continue
            found.append((mtime, path))

    found.sort(key=lambda item: item[0], reverse=True)
    found = found[:max_notes]

    notes = []
    for mtime, path in found:
        raw = read_text(path)
        title = extract_title(raw, path.stem)
        excerpt = clean_note(raw)
        if excerpt.startswith(title):
            excerpt = excerpt[len(title):].lstrip(" :-")
        if len(excerpt.split()) < 15:
            continue
        rel = path.relative_to(vault).as_posix()
        notes.append(
            {
                "path": rel,
                "title": title,
                "excerpt": " ".join(excerpt.split()[:words]),
                "days_ago": max(0, int((now.timestamp() - mtime) // 86400)),
                "mtime": int(mtime),
            }
        )

    return {
        "vault": str(vault),
        "today": compact_date(now),
        "iso_date": iso_date(now),
        "generated_at": now.isoformat(timespec="seconds"),
        "lookback_days": days,
        "notes": notes,
    }


# --------------------------------------------------------------------------
# History and sampling
# --------------------------------------------------------------------------


def history_path(vault):
    return Path(vault) / HISTORY_REL


def read_history(vault):
    path = history_path(vault)
    if not path.exists():
        return {"sampled_pairs": [], "runs": []}
    try:
        data = read_json(path)
    except (OSError, ValueError) as exc:
        eprint(f"WARN: history is unreadable ({exc}); starting fresh")
        return {"sampled_pairs": [], "runs": []}
    if not isinstance(data, dict):
        return {"sampled_pairs": [], "runs": []}
    data.setdefault("sampled_pairs", [])
    data.setdefault("runs", [])
    return data


def pair_key(a, b):
    left, right = sorted([str(a).replace("\\", "/").lower(), str(b).replace("\\", "/").lower()])
    return (left, right)


def sample_pairs(notes, count, history, seed=None):
    if len(notes) < 2:
        raise SystemExit("Need at least 2 notes to form a pair.")

    rng = random.Random(seed)
    weights = []
    for note in notes:
        days = note.get("days_ago", 999)
        weights.append(3 if days <= 7 else 2 if days <= 30 else 1)

    pool = []
    for index, weight in enumerate(weights):
        pool.extend([index] * weight)

    known = set()
    for item in history.get("sampled_pairs", []):
        if isinstance(item, dict) and item.get("a") and item.get("b"):
            known.add(pair_key(item["a"], item["b"]))

    pairs = []
    used = set()
    target = min(count, len(notes) * (len(notes) - 1) // 2)

    # For small vaults, enumerate all candidates and drop known pairs first.
    if len(notes) <= 64:
        candidates = []
        for i in range(len(notes)):
            for j in range(i + 1, len(notes)):
                key = pair_key(notes[i]["path"], notes[j]["path"])
                if key not in known:
                    candidates.append((i, j))
        rng.shuffle(candidates)
        for i, j in candidates[:target]:
            pairs.append((i, j))
            used.add(pair_key(notes[i]["path"], notes[j]["path"]))
        return pairs

    attempts = 0
    limit = max(1000, target * 400)
    while len(pairs) < target and attempts < limit:
        attempts += 1
        i = rng.choice(pool)
        j = rng.choice(pool)
        if i == j:
            continue
        key = pair_key(notes[i]["path"], notes[j]["path"])
        if key in used or key in known:
            continue
        used.add(key)
        pairs.append((i, j))

    return pairs


# --------------------------------------------------------------------------
# Saving results
# --------------------------------------------------------------------------


def normalise_insights(results):
    if isinstance(results, dict):
        items = results.get("insights") or results.get("results") or []
    elif isinstance(results, list):
        items = results
    else:
        items = []
    return [item for item in items if isinstance(item, dict)]


def score_average(item):
    try:
        average = float(item.get("average"))
    except (TypeError, ValueError):
        values = []
        for key in ("novelty", "coherence", "usefulness"):
            try:
                values.append(float(item.get(key)))
            except (TypeError, ValueError):
                pass
        average = sum(values) / len(values) if len(values) == 3 else 0.0
    return round(average, 1)


def normalise_insight(item):
    insight = dict(item)
    insight["title"] = (
        item.get("title")
        or item.get("suggested_title")
        or item.get("connection")
        or "Untitled daydream"
    )
    insight["title"] = " ".join(str(insight["title"]).split())[:120]
    insight["title_a"] = item.get("title_a") or item.get("a_title") or "Note A"
    insight["title_b"] = item.get("title_b") or item.get("b_title") or "Note B"
    insight["connection"] = item.get("connection") or insight["title"]
    insight["synthesis"] = item.get("synthesis") or item.get("connection") or ""
    insight["implication"] = item.get("implication") or ""
    insight["reason"] = item.get("reason") or item.get("critic_note") or ""
    for key in ("novelty", "coherence", "usefulness"):
        try:
            insight[key] = float(item.get(key))
        except (TypeError, ValueError):
            insight[key] = 0.0
    insight["average"] = score_average(item)
    verdict = str(item.get("verdict") or "").strip().lower()
    insight["verdict"] = verdict or ("accept" if insight["average"] >= SCORE_THRESHOLD else "reject")
    return insight


def render_insight(insight, today):
    lines = [
        "---",
        f"created_date: {iso_date(parse_date(today))}",
        "type: daydream",
        "source_notes:",
        f"  - {yaml_string('[[' + str(insight['title_a']) + ']]')}",
        f"  - {yaml_string('[[' + str(insight['title_b']) + ']]')}",
        "scores:",
        f"  novelty: {insight['novelty']:g}",
        f"  coherence: {insight['coherence']:g}",
        f"  usefulness: {insight['usefulness']:g}",
        f"  average: {insight['average']:g}",
        "---",
        "",
        f"# {insight['title']}",
        "",
        f"> Connection between [[{insight['title_a']}]] and [[{insight['title_b']}]]",
        "",
        insight["synthesis"].strip(),
        "",
    ]
    if insight["implication"]:
        lines += ["## Implication", "", insight["implication"].strip(), ""]
    if insight["reason"]:
        lines += ["## Critic's Note", "", insight["reason"].strip(), ""]
    return "\n".join(lines).rstrip() + "\n"


def render_digest_run(today, total_pairs, total_synthesized, accepted, now, threshold=SCORE_THRESHOLD):
    rate = (len(accepted) / total_pairs * 100) if total_pairs else 0.0
    lines = [
        f"## Run {now.strftime('%H:%M')}",
        "",
        "### Stats",
        f"- Pairs sampled: {total_pairs}",
        f"- Insights generated: {total_synthesized}",
        f"- Accepted (avg >= {threshold:g}): {len(accepted)}",
        f"- Acceptance rate: {rate:.1f}%",
        "",
        "### Top Insights",
        "",
    ]
    ranked = sorted(accepted, key=lambda item: item["average"], reverse=True)
    if not ranked:
        lines.append("_No insight cleared the score threshold this run._")
        lines.append("")
    for index, insight in enumerate(ranked, 1):
        lines += [
            f"#### {index}. {insight['title']} (avg: {insight['average']:g})",
            f"**Connecting**: [[{insight['title_a']}]] <-> [[{insight['title_b']}]]",
            "",
            insight["connection"].strip(),
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def find_daily_note(vault, daily_dir, today):
    directory = Path(daily_dir)
    if not directory.is_absolute():
        directory = Path(vault) / directory
    if not directory.is_dir():
        return None, directory

    compact = today
    parsed = parse_date(today) or datetime.now()
    candidates = [
        f"{compact}.md",
        f"{parsed.strftime('%Y-%m-%d')}.md",
        f"{parsed.strftime('%Y_%m_%d')}.md",
        f"{parsed.strftime('%Y.%m.%d')}.md",
    ]
    for name in candidates:
        candidate = directory / name
        if candidate.exists():
            return candidate, directory

    # Fall back to a case-insensitive match.
    lowered = {name.lower() for name in candidates}
    for candidate in sorted(directory.glob("*.md")):
        if candidate.name.lower() in lowered:
            return candidate, directory
    return None, directory


def update_daily_note(vault, daily_dir, today, accepted, total_pairs):
    note, directory = find_daily_note(vault, daily_dir, today)
    if note is None:
        if not directory.is_dir():
            return None
        parsed = parse_date(today) or datetime.now()
        note = directory / f"{parsed.strftime('%Y-%m-%d')}.md"
        write_text(note, f"# {parsed.strftime('%Y-%m-%d')}\n")

    rate = (len(accepted) / total_pairs * 100) if total_pairs else 0.0
    noun = "insight" if len(accepted) == 1 else "insights"
    lines = [
        "## Daydream",
        "",
        f"Vault daydream found {len(accepted)} {noun} from {total_pairs} pairs "
        f"({rate:.1f}% acceptance).",
        "",
    ]
    ranked = sorted(accepted, key=lambda item: item["average"], reverse=True)[:5]
    if ranked:
        for insight in ranked:
            slug = slugify(insight["title"])
            lines.append(
                f"- [[{compact_date(parse_date(today))}-{slug}|{insight['title']}]] "
                f"(avg: {insight['average']:g}) -- [[{insight['title_a']}]] <-> "
                f"[[{insight['title_b']}]]"
            )
    else:
        lines.append("_No insight cleared the threshold this run._")

    section = "\n".join(lines).rstrip() + "\n"
    text = read_text(note)
    pattern = re.compile(r"(?ms)^## Daydream[ \t]*\r?\n.*?(?=^## |\Z)")
    if pattern.search(text):
        text = pattern.sub(section + "\n", text, count=1)
    else:
        text = text.rstrip() + "\n\n" + section
    write_text(note, text)
    return note


def save_results(vault, pairs_file, results_files, threshold, daily_dir, update_daily):
    pairs_data = read_json(pairs_file)

    raw_insights = []
    for results_file in results_files:
        raw_insights.extend(normalise_insights(read_json(results_file)))

    pairs = pairs_data.get("pairs", [])
    total_pairs = len(pairs)
    today = pairs_data.get("today") or compact_date()
    now = datetime.now()

    total_synthesized = len(raw_insights)
    accepted = []
    for item in raw_insights:
        insight = normalise_insight(item)
        if insight["verdict"] == "reject":
            continue
        if insight["average"] < threshold:
            continue
        accepted.append(insight)

    daydreams = Path(vault) / DAYDREAMS_REL
    digests = Path(vault) / DIGESTS_REL
    digests.mkdir(parents=True, exist_ok=True)

    written = []
    for insight in accepted:
        slug = slugify(insight["title"])
        path = daydreams / f"{today}-{slug}.md"
        counter = 2
        while path.exists():
            path = daydreams / f"{today}-{slug}-{counter}.md"
            counter += 1
        write_text(path, render_insight(insight, today))
        written.append(str(path))

    digest = digests / f"{today}-digest.md"
    run_block = render_digest_run(today, total_pairs, total_synthesized, accepted, now, threshold=threshold)
    if digest.exists():
        existing = read_text(digest).rstrip()
        write_text(digest, existing + "\n\n---\n\n" + run_block)
    else:
        header = [
            "---",
            "type: daydream-digest",
            f"date: {iso_date(parse_date(today))}",
            f"pairs_sampled: {total_pairs}",
            f"insights_accepted: {len(accepted)}",
            "---",
            "",
            f"# Daydream Digest - {iso_date(parse_date(today))}",
            "",
        ]
        write_text(digest, "\n".join(header) + "\n" + run_block)

    daily_note = None
    if update_daily:
        daily_note = update_daily_note(vault, daily_dir, today, accepted, total_pairs)

    history = read_history(vault)
    existing_keys = set()
    for item in history["sampled_pairs"]:
        if isinstance(item, dict) and item.get("a") and item.get("b"):
            existing_keys.add(pair_key(item["a"], item["b"]))
    for pair in pairs:
        a = pair.get("a", {}).get("path")
        b = pair.get("b", {}).get("path")
        if not a or not b:
            continue
        key = pair_key(a, b)
        if key in existing_keys:
            continue
        existing_keys.add(key)
        history["sampled_pairs"].append({"a": a, "b": b, "date": today})

    rate = (len(accepted) / total_pairs * 100) if total_pairs else 0.0
    history["runs"].append(
        {
            "date": today,
            "timestamp": now.isoformat(timespec="seconds"),
            "pairs_sampled": total_pairs,
            "insights_generated": total_synthesized,
            "insights_accepted": len(accepted),
            "acceptance_rate": round(rate, 1),
        }
    )
    write_json(history_path(vault), history)

    return {
        "vault": str(vault),
        "today": today,
        "pairs_sampled": total_pairs,
        "insights_generated": total_synthesized,
        "insights_accepted": len(accepted),
        "acceptance_rate": round(rate, 1),
        "insight_files": written,
        "digest": str(digest),
        "daily_note": str(daily_note) if daily_note else None,
        "top_insights": [
            {
                "title": item["title"],
                "average": item["average"],
                "title_a": item["title_a"],
                "title_b": item["title_b"],
            }
            for item in sorted(accepted, key=lambda x: x["average"], reverse=True)[:5]
        ],
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def command_resolve(args):
    if args.set:
        target = Path(args.set).expanduser().resolve()
        if not target.is_dir():
            raise SystemExit(f"Cannot save vault; not a directory: {target}")
        config = load_config()
        config["vault"] = str(target)
        saved = save_config(config)
        print(
            json.dumps(
                {
                    "vault": str(target),
                    "is_obsidian_vault": is_vault(target),
                    "config": str(saved),
                },
                indent=2,
            )
        )
        return

    vault = find_vault(args.vault)
    print(
        json.dumps(
            {
                "vault": str(vault),
                "is_obsidian_vault": is_vault(vault),
                "config": str(config_path()),
            },
            indent=2,
        )
    )


def command_scan(args):
    vault = find_vault(args.vault)
    data = scan_notes(
        vault,
        days=args.days,
        max_notes=args.max_notes,
        words=args.words,
    )
    out = Path(args.out) if args.out else default_workfile("scan", data["today"])
    write_json(out, data)
    print(
        json.dumps(
            {
                "vault": str(vault),
                "notes_found": len(data["notes"]),
                "out": str(out),
                "today": data["today"],
            },
            indent=2,
        )
    )


def command_sample(args):
    scan = read_json(args.scan)
    notes = scan.get("notes", [])
    vault = Path(scan.get("vault") or find_vault(args.vault))
    history = read_history(vault)
    indices = sample_pairs(notes, args.pairs, history, seed=args.seed)
    pairs = [{"a": notes[i], "b": notes[j]} for i, j in indices]
    today = scan.get("today") or compact_date()
    out = Path(args.out) if args.out else default_workfile("pairs", today)
    data = {
        "vault": str(vault),
        "today": today,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "notes_available": len(notes),
        "requested_pairs": args.pairs,
        "pairs": pairs,
        "out": str(out),
    }
    write_json(out, data)
    print(
        json.dumps(
            {
                "vault": str(vault),
                "notes_available": len(notes),
                "pairs": len(pairs),
                "out": str(out),
                "today": today,
            },
            indent=2,
        )
    )


def command_batch(args):
    data = read_json(args.pairs)
    pairs = data.get("pairs", [])
    start = max(0, args.start)
    chunk = pairs[start:start + args.count]
    if not chunk:
        print(f"No pairs at offset {start} (total: {len(pairs)}).")
        return
    print(f"PAIRS {start + 1}-{start + len(chunk)} of {len(pairs)}")
    for offset, pair in enumerate(chunk, start + 1):
        a, b = pair.get("a", {}), pair.get("b", {})
        print("")
        print(f"=== PAIR {offset} ===")
        print(f"A: {a.get('title')} ({a.get('path')})")
        print(a.get("excerpt", ""))
        print(f"B: {b.get('title')} ({b.get('path')})")
        print(b.get("excerpt", ""))
        print("=== END PAIR ===")


def command_save(args):
    vault = find_vault(args.vault)
    summary = save_results(
        vault,
        args.pairs,
        args.results,
        threshold=args.threshold,
        daily_dir=args.daily_dir,
        update_daily=not args.no_daily,
    )
    print(json.dumps(summary, indent=2))

def command_stats(args):
    vault = find_vault(args.vault)
    history = read_history(vault)
    runs = history.get("runs", [])
    total_pairs = len(history.get("sampled_pairs", []))
    print(
        json.dumps(
            {
                "vault": str(vault),
                "runs": len(runs),
                "pairs_logged": total_pairs,
                "last_runs": runs[-args.limit:],
            },
            indent=2,
        )
    )


def build_parser():
    parser = argparse.ArgumentParser(
        prog="daydream",
        description="Scan, sample, and save Vault Daydream runs.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    resolve = sub.add_parser("resolve", help="Find the Obsidian vault.")
    resolve.add_argument("--vault", help="Explicit vault path.")
    resolve.add_argument("--set", help="Save this path as the default vault.")
    resolve.set_defaults(func=command_resolve)

    scan = sub.add_parser("scan", help="Scan recent notes.")
    scan.add_argument("--vault", help="Explicit vault path.")
    scan.add_argument("--days", type=int, default=LOOKBACK_DAYS)
    scan.add_argument("--max-notes", type=int, default=MAX_NOTES)
    scan.add_argument("--words", type=int, default=MAX_EXCERPT_WORDS)
    scan.add_argument("--out", help="Output JSON path.")
    scan.set_defaults(func=command_scan)

    sample = sub.add_parser("sample", help="Sample note pairs.")
    sample.add_argument("--scan", required=True, help="Scan JSON from `scan`.")
    sample.add_argument("--vault", help="Override vault path.")
    sample.add_argument("--pairs", type=int, default=PAIR_COUNT)
    sample.add_argument("--seed", type=int, help="Random seed for reproducibility.")
    sample.add_argument("--out", help="Output JSON path.")
    sample.set_defaults(func=command_sample)

    batch = sub.add_parser("batch", help="Print pairs for synthesis.")
    batch.add_argument("--pairs", required=True, help="Pairs JSON from `sample`.")
    batch.add_argument("--start", type=int, default=0)
    batch.add_argument("--count", type=int, default=5)
    batch.set_defaults(func=command_batch)

    save = sub.add_parser("save", help="Write insights, digest, daily note, history.")
    save.add_argument("--vault", help="Explicit vault path.")
    save.add_argument("--pairs", required=True, help="Pairs JSON from `sample`.")
    save.add_argument("--results", required=True, nargs="+", help="One or more scored insight JSON files.")
    save.add_argument("--threshold", type=float, default=SCORE_THRESHOLD)
    save.add_argument("--daily-dir", default="Daily", help="Daily note folder.")
    save.add_argument("--no-daily", action="store_true", help="Skip the daily note.")
    save.set_defaults(func=command_save)

    stats = sub.add_parser("stats", help="Show run history.")
    stats.add_argument("--vault", help="Explicit vault path.")
    stats.add_argument("--limit", type=int, default=5)
    stats.set_defaults(func=command_stats)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
