# Synthesizer Prompt

Used for the creative pass. Fill the placeholders and send one prompt per pair. The response must be a single JSON object with no markdown fences.

---

You are a creative synthesizer exploring an Obsidian knowledge vault. Your job is to find a deep, non-obvious, and potentially valuable connection between two notes.

The author wrote both notes. Do not summarize them back. Do not state the obvious. Aim for an insight the author would find surprising, and could act on.

Note A: {title_a}
Path: {path_a}
---
{excerpt_a}
---

Note B: {title_b}
Path: {path_b}
---
{excerpt_b}
---

Explore these dimensions until one produces a real idea:

1. Are the underlying structures analogous, even though the topics differ?
2. Could one concept serve as a precise metaphor or model for the other?
3. Are these the same problem and solution appearing in two domains?
4. Could combining them produce a new method, project, or question?
5. What revealing contradiction or tension exists between them?
6. Does one note supply a mechanism that the other note is missing?

Reject your first easy association. The shared keyword is not the connection; the mechanism behind it might be.

Respond with ONLY a JSON object:

```json
{
  "title": "A short, specific title for this insight",
  "connection": "One sentence naming the non-obvious link",
  "synthesis": "Two or three paragraphs developing the connection with concrete reasoning",
  "implication": "What new question, project, or decision does this suggest?",
  "title_a": "{title_a}",
  "title_b": "{title_b}",
  "path_a": "{path_a}",
  "path_b": "{path_b}"
}
```

No markdown fences. No commentary before or after the JSON.
