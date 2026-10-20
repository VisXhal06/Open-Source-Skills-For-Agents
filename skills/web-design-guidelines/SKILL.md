---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## Anti-generic gate

Compliance is not visual quality. Also flag generic AI defaults unless the project's own system requires them:

- **Type:** Inter, Roboto, Arial, Helvetica, or a system stack; the Poppins / Montserrat / Open Sans / Lato stack; chosen with no subject-specific reason.
- **Color:** violet, indigo, or purple on white; a blue-to-purple "AI" gradient; gradient text; a pastel mesh.
- **Layout:** the centered badge-headline-two-buttons hero; three identical feature cards; a logo cloud; a testimonial trio; a pricing trio with a highlighted middle card; identical bento tiles; a floating dashboard mockup.
- **Components:** a pill above every heading; one radius and shadow everywhere; an icon in a rounded square for every feature; gradient-border cards; hover-lift everywhere.
- **Motion:** fade-and-slide-up everywhere; stagger everywhere; a looping ambient gradient.
- **Copy:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a claim.

Report as `file:line — anti-generic: <pattern>. Replace with <specific move>.` If the project's design system mandates the pattern, do not flag it; note the exception. A banned default that defines the first impression is a blocker; a localized one is a major finding.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines and the anti-generic gate above
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
