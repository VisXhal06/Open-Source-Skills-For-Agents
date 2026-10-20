---
name: vault-daydream
description: Mine an Obsidian vault for non-obvious connections between notes. Samples recency-weighted note pairs, synthesizes original insights, scores them with a skeptical critic, and saves the best to Daydreams/ with a digest and daily-note summary. Use for /daydream, "daydream my vault", "find connections in my notes", or creative vault mining.
metadata:
  trigger: /daydream, "daydream my vault", "find connections between my notes", "vault daydream"
  source: https://github.com/glebis/claude-skills/tree/main/daydream
---

# Vault Daydream

Turn a vault into a idea generator. The skill samples pairs of recent notes that have never been paired before, looks for a genuinely non-obvious connection, then scores the result and keeps only what survives a skeptical review. Inspired by [Gwern's LLM daydreaming](https://gwern.net/ai-daydreaming).

## When to use

Use when the user wants serendipitous cross-note insight rather than search:

- `/daydream` or "daydream my vault"
- "What connections am I missing between my notes?"
- "Generate ideas from my Obsidian vault"
- A scheduled weekly creative pass over a knowledge base

Do not use for retrieving a specific note, summarizing a folder, or answering a factual question. Use search or the `understand` skills for that.

## Requirements

- An Obsidian vault (a folder containing `.obsidian/`), or any folder of markdown notes passed explicitly.
- Python 3.8+ on PATH (`python` or `python3`). The helper is stdlib-only; no packages to install.
- No network calls. Everything runs locally against the vault.

Paths below use `<skill-dir>`. Replace it with the absolute path of the folder containing this `SKILL.md`; the harness reports that location when the skill is loaded.

## Setup once

Resolve the vault and remember it:

```bash
python "<skill-dir>/scripts/daydream.py" resolve --set "/path/to/vault"
```

Resolution order is: `--vault` flag, then `DAYDREAM_VAULT`, then the saved config, then walking up from the current directory, then a shallow search of common folders. If nothing is found, the command prints the three ways to fix it.

## Workflow

Run these steps in order. Full orchestration detail lives in `instructions.md`; the scoring rubric lives in `critic-prompt.md`.

1. **Scan.** `daydream.py scan` finds markdown notes modified in the last 120 days (max 200, newest first), strips frontmatter/code/URLs, and extracts titles plus 500-word excerpts.

```bash
python "<skill-dir>/scripts/daydream.py" scan --out "$TEMP/daydream/scan.json"
```

2. **Sample.** `daydream.py sample` builds recency-weighted pairs (notes from the last week count 3x, last month 2x, older 1x), skips pairs already logged in `ai-research/daydream/history.json`, and defaults to 30 pairs. Use `--pairs 10` for a quick pass or `--pairs 50` for a deep one.

```bash
python "<skill-dir>/scripts/daydream.py" sample --scan scan.json --pairs 30 --out pairs.json
```

3. **Synthesize.** Read `synthesizer-prompt.md`. Work through the pairs with `daydream.py batch --pairs pairs.json --start N --count 5`, producing 2-3 paragraph syntheses. Write raw JSON to `results.json` as you go.

4. **Critique.** Read `critic-prompt.md`. Score each insight 1-10 on novelty, coherence, and usefulness. Be harsh: random pairs should usually be rejected. Prefer a fresh subagent for this pass when the harness has one; otherwise re-read the insights cold and score them in a second pass.

5. **Save.** `daydream.py save` filters at average >= 7.0, writes one note per accepted insight to `Daydreams/YYYYMMDD-slug.md`, appends a run to `Daydreams/digests/YYYYMMDD-digest.md`, updates the `## Daydream` section of today's daily note when a `Daily/` folder exists, and logs every sampled pair.

```bash
python "<skill-dir>/scripts/daydream.py" save --pairs pairs.json --results results.json
```

6. **Report.** Give the user the accepted count, acceptance rate, and the top three connections with wikilinks. Link the digest and insight files.

## Output contract

```text
Daydreams/YYYYMMDD-slug.md          one note per accepted insight (scores in frontmatter)
Daydreams/digests/YYYYMMDD-digest.md  per-day digest; repeat runs append a "## Run HH:MM" section
ai-research/daydream/history.json     sampled pairs + run stats, used to avoid repeats
Daily/<today>.md                      optional "## Daydream" section, replaced on re-run
```

## Scoring

Each insight gets three 1-10 scores. Average >= 7.0 is accepted.

- **Novelty**: Would the author be surprised? 1 = obvious, 10 = reframes how they think.
- **Coherence**: Does the argument hold? 1 = word salad, 10 = rigorous.
- **Usefulness**: Does it suggest an action, project, or question? 1 = trivia, 10 = changes what they do next.

An insight that is merely a shared keyword ("both involve growth") is a rejection, no matter how well written.

## Rules

- **Use the real excerpts.** Never invent note content, titles, or paths.
- **Do not edit or delete source notes.** Only write under `Daydreams/`, the daily note, and `ai-research/daydream/`.
- **One connection per pair.** Do not recycle the same idea across pairs.
- **No forced insight.** A 10% acceptance rate is healthy. Zero accepted is a valid result.
- **Keep quotes short.** Synthesize in your own words; do not paste long note passages into the output.
- **Respect privacy.** The vault stays local; do not upload excerpts anywhere.

## Failure modes

| Symptom | Fix |
| --- | --- |
| "No Obsidian vault found" | Run from inside the vault, set `DAYDREAM_VAULT`, or `resolve --set`. |
| Fewer than 10 notes | The run still works but is repetitive; widen `--days` or lower `--pairs`. |
| All pairs already sampled | Expected on frequent runs; history grows. Wait, add notes, or delete old `sampled_pairs` entries. |
| Every insight rejected | Normal. Try more diverse notes or a different pair count; do not lower the threshold. |
| Malformed results JSON | Fix the JSON or drop the bad batch; `save` ignores entries without usable scores. |

## Cost and time

A 30-pair run reads about 60 excerpts and produces roughly 10-30k tokens of reasoning, depending on the model. Inline runs take a few minutes. Delegating synthesis and critique to parallel subagents is faster but uses more context; keep batches at five pairs.
