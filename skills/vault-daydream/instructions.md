# Vault Daydream: Orchestration Instructions

You are running the Vault Daydream skill. Follow these steps in order. The Python helper does everything deterministic; you supply the creative synthesis and the skeptical scoring.

Throughout, `<skill-dir>` means the folder containing this file. On a typical install:

- Windows: `C:\Users\<you>\.agents\skills\vault-daydream`
- macOS/Linux: `~/.agents/skills/vault-daydream`

Use `python` if that is the available interpreter, otherwise `python3`.

---

## Step 0: Resolve the vault

```bash
python "<skill-dir>/scripts/daydream.py" resolve
```

The command searches, in order: `--vault`, `DAYDREAM_VAULT`, saved config, the current directory and its parents, then common folders. If it fails, ask the user for the vault path, then run:

```bash
python "<skill-dir>/scripts/daydream.py" resolve --set "<path>"
```

Do not scan a folder the user did not confirm as their vault.

---

## Step 1: Scan

```bash
python "<skill-dir>/scripts/daydream.py" scan
```

Output JSON includes the `out` path, `notes_found`, and `today`. Keep that path as `SCAN`.

- 0 notes: stop and report "No notes modified in the last 120 days. Nothing to daydream about."
- 1-9 notes: warn that the vault is small, use `--pairs 5`.
- For a wider net, add `--days 365`. For a focused pass, add `--days 30`.

Each note in the scan has `path`, `title`, `excerpt`, `days_ago`, `mtime`.

---

## Step 2: Sample pairs

```bash
python "<skill-dir>/scripts/daydream.py" sample --scan "<SCAN>" --pairs 30
```

Keep the printed `out` path as `PAIRS`. The sampler:

- weights notes from the last 7 days 3x, last 30 days 2x, older 1x
- excludes pairs already recorded in `ai-research/daydream/history.json`
- caps at the number of possible pairs
- is deterministic only when `--seed` is passed

Use 10 pairs for a quick pass, 30 for the default, 50 for a deep run.

---

## Step 3: Synthesize, batch by batch

Read `synthesizer-prompt.md` once. Then process the pairs five at a time.

Print a batch:

```bash
python "<skill-dir>/scripts/daydream.py" batch --pairs "<PAIRS>" --start 0 --count 5
```

For each pair, fill the synthesizer prompt with the two titles and excerpts, and produce:

```json
{
  "title": "Short, specific insight title",
  "title_a": "Title A",
  "title_b": "Title B",
  "path_a": "relative/path-a.md",
  "path_b": "relative/path-b.md",
  "connection": "One sentence naming the non-obvious link.",
  "synthesis": "Two or three paragraphs developing the link.",
  "implication": "A concrete question, project, or decision this suggests."
}
```

Rules for the synthesis:

- Look for structural similarity, shared tension, transferable mechanism, or productive contradiction. Not shared keywords.
- Be specific to these two notes. If the paragraph would survive swapping in two unrelated notes, it is too generic.
- Do not summarize the notes. The user already wrote them.
- No bullet lists, no headings, no markdown fences inside `synthesis`.
- One idea per pair. If a pair supports two ideas, pick the stronger one.

Write each batch to its own file, e.g. `results-01.json`, using the array shape below. Write files where the agent can access them (the system temp folder is fine); keep the paths.

```json
{
  "insights": [
    {
      "title": "...",
      "title_a": "...",
      "title_b": "...",
      "path_a": "...",
      "path_b": "...",
      "connection": "...",
      "synthesis": "...",
      "implication": "...",
      "novelty": 8,
      "coherence": 8,
      "usefulness": 7,
      "average": 7.7,
      "verdict": "accept",
      "reason": "One sentence explaining the score."
    }
  ]
}
```

If a pair yields nothing defensible, still emit an entry with `verdict: "reject"`, a low average, and the reason. Rejections are data, not failures.

### Parallel option

If the harness exposes a subagent/task tool, launch one subagent per batch with the synthesizer prompt and that batch's text. Collect its JSON array. Do not let subagents read the vault directly; pass them the excerpts so every run sees identical input. Keep batches at five pairs to stay inside context limits.

---

## Step 4: Critique and score

Read `critic-prompt.md`. Score each insight on novelty, coherence, and usefulness (1-10 each), compute the average to one decimal, and set `verdict` to `accept` only when the average is 7.0 or higher.

Prefer an independent pass:

- With a subagent tool: send the critic prompt plus the batch's insights, and ask for JSON only. Use the returned scores.
- Without one: finish all synthesis first, then re-read each batch cold and score it. Do not score while still attached to the idea.

Scoring discipline:

- 7+ requires a genuinely surprising link **and** a usable implication. Most random pairs should score 4-6.
- Penalize restatement, vague analogy, and "both are about growth" connections.
- Reward a precise mechanism, a real tension, or a decision that changes.
- Do not inflate scores to make the run look successful. A 0-20% acceptance rate is normal.

Merge the critic scores into each insight object and write the final batch file. All scored insights, accepted and rejected, go into the results files; `save` applies the threshold.

---

## Step 5: Save

```bash
python "<skill-dir>/scripts/daydream.py" save --pairs "<PAIRS>" --results results-01.json results-02.json ...
```

Useful flags:

- `--threshold 7.0` (default)
- `--daily-dir Daily` (default; relative to the vault)
- `--no-daily` to skip touching the daily note

The command:

1. filters to `verdict != reject` and `average >= threshold`
2. writes `Daydreams/YYYYMMDD-slug.md` per accepted insight, with scores in frontmatter
3. appends a run section to `Daydreams/digests/YYYYMMDD-digest.md`
4. replaces or appends the `## Daydream` section of today's daily note, if a daily folder exists
5. logs all sampled pairs and the run stats to `ai-research/daydream/history.json`

It prints a summary JSON with `insights_accepted`, `acceptance_rate`, `insight_files`, `digest`, `daily_note`, and `top_insights`. Use those exact values in your report; do not recount by hand.

---

## Step 6: Report

Keep it short:

```text
Vault Daydream - 2026-10-20

4 of 30 pairs cleared 7.0 (13.3% acceptance).

Top insights:
1. <title> (8.7) - <note A> <-> <note B>
2. ...
3. ...

Files: Daydreams/20261020-*.md
Digest: Daydreams/digests/20261020-digest.md
```

Mention if the daily note was updated. Mention if zero insights were accepted, without apologizing; that is a legitimate outcome.

---

## Error handling

| Situation | Action |
| --- | --- |
| Vault not found | Ask for the path, then `resolve --set`. |
| Scan finds 0 notes | Stop with the "nothing to daydream about" message. |
| Scan finds 1 note | Stop; pairs require two notes. |
| Fewer pairs than requested | Proceed with what was sampled; say so. |
| A batch returns malformed JSON | Rewrite that batch once. If it still fails, skip it and note the skip in the report. |
| All insights rejected | Save anyway (digest records the zero), then report it plainly. |
| `save` warns about unreadable history | It starts fresh; tell the user the old history was not used. |
| Daily note has no `## Daydream` section | The script appends one; no manual edit needed. |
| Re-running the same day | Insight filenames get `-2`, `-3`; the daily section is replaced; the digest gains a new run section. |

## Hard rules

- Never fabricate note content, titles, or paths.
- Never modify source notes, templates, or `.obsidian/`.
- Only write under `Daydreams/`, `ai-research/daydream/`, and the daily note.
- Keep the vault local. Do not send excerpts to external services.
- Do not lower the threshold to manufacture a result.
