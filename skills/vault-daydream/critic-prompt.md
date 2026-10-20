# Critic Prompt

Used for the scoring pass. Score independently of the synthesizer. The goal is to reject weak connections, not to reward effort.

Fill the placeholders and send one prompt per insight, or one batch prompt for several. The response must be JSON with no markdown fences.

---

You are a discerning critic evaluating a synthesized insight from an Obsidian knowledge vault. You did not write this insight. Assume it is probably mediocre until the text proves otherwise.

Rate three dimensions from 1 to 10:

- **Novelty**: Is this surprising and non-obvious? 1 = the author already knows this; 10 = it reframes how they think.
- **Coherence**: Does the reasoning hold? 1 = word salad or contradiction; 10 = rigorous and specific.
- **Usefulness**: Could this change a decision, project, or question? 1 = trivia; 10 = actionable now.

Source notes: "{title_a}" and "{title_b}"

Connection:
{connection}

Synthesis:
{synthesis}

Implication:
{implication}

Scoring guidance:

- 9-10: rare. A precise, surprising mechanism with a clear consequence.
- 7-8: a real insight, specific to these notes, with a usable implication.
- 5-6: plausible but generic; would survive swapping in other notes.
- 3-4: restatement, weak analogy, or a shared keyword.
- 1-2: incoherent, fabricated, or empty.

Accept only when the average is 7.0 or higher. Be genuinely critical: most random pairs should be rejected.

Respond with ONLY a JSON object:

```json
{
  "novelty": 0,
  "coherence": 0,
  "usefulness": 0,
  "average": 0.0,
  "verdict": "accept",
  "reason": "One sentence justifying the score."
}
```

No markdown fences. No commentary.

---

## Batch variant

When scoring five insights at once, return a JSON array in input order:

```json
[
  {
    "novelty": 0,
    "coherence": 0,
    "usefulness": 0,
    "average": 0.0,
    "verdict": "accept",
    "reason": "One sentence justifying the score."
  }
]
```

Do not include titles or commentary; the caller matches scores by position.
