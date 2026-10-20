# handoff

A Claude skill that generates a complete handoff document of your current conversation, so another LLM (ChatGPT, a fresh Claude session, Gemini, anything) can pick up exactly where this one left off.

Hitting the context limit mid-task is the worst moment to lose your work. This skill turns the whole session into one portable markdown document: the goal, every decision made, the exact current draft or code (verbatim, not summarized), what was already tried and rejected, and the single next step. Paste it into any model and keep going.

## What you get

One markdown file with these sections:

- **Context & goal**: who you are and what you're trying to accomplish
- **Key decisions made**: settled choices the next model must not re-litigate
- **Current state**: what's done, what's validated, what's mid-flight
- **Work in progress (verbatim)**: the full exact draft, code, or plan, word for word
- **Rejected paths**: what was tried and abandoned, so it doesn't get proposed again
- **Tone & working preferences**: how you like to work, phrased as instructions
- **Immediate next step**: the first thing the next model should do

The skill enforces zero invention: only facts that literally appear in the conversation make it into the document.

## Install

### Claude Code

Clone straight into your personal skills folder:

```bash
git clone https://github.com/ToolMonsters/handoff-skill ~/.claude/skills/handoff
```

Or for a single project, clone into `.claude/skills/handoff` inside the repo.

### Claude apps (claude.ai / desktop)

Upload the `SKILL.md` file as a skill in **Settings → Capabilities → Skills**.

## Use

Type any of these in a conversation:

```
/handoff
```

or just say "handoff", "I'm about to hit the context limit", or "I want to continue this in ChatGPT".

Claude writes `handoff-[topic].md`. Open your next session anywhere, paste the document, and continue.

## Why the "verbatim" rule matters

Most handoff attempts fail because the summary describes the work instead of carrying it. A description of your draft forces the next model to regenerate it, and it never comes back the same. This skill requires the full exact text of anything in progress, which is the difference between resuming and restarting.

## License

MIT

---

Made by Yonathan Cohen (Tool Monsters)
