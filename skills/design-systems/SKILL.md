---
name: design-systems
description: "Use when building or maintaining a design system, design tokens, component library, theme, Figma-to-code workflow, or an AI-readable design system that keeps generated UI consistent."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Design Systems

Build a system that makes good design the default and bad design hard. This skill covers tokens, primitives, components, documentation, governance, Figma/code parity, and AI-readable system context.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks about tokens, components, consistency, themes, or Figma-to-code. Direct invocation works too. If a visual direction exists, turn it into a system here.

## The system layers

| Layer | What it is | Example |
| --- | --- | --- |
| Principles | The values that resolve trade-offs | “Density with breathing room” |
| Tokens | Named design decisions | `color.text.muted`, `space.4` |
| Primitives | Unstyled or lightly styled building blocks | Button behavior, focus ring, popover positioning |
| Components | Composed, reusable UI | Button, Input, Dialog, Card |
| Patterns | Repeated combinations for a job | Empty state, settings row, checkout summary |
| Documentation | How and when to use the system | Anatomy, usage, do/don't, accessibility |
| Governance | How the system changes | Contribution, review, versioning, deprecation |

Do not start with components. Start with principles and tokens.

## Step 1: Audit what exists

Before building, inventory:

- Colors actually used, including hardcoded hex values.
- Type sizes, weights, and line heights.
- Spacing values.
- Radii, borders, shadows.
- Components and their variants.
- States that exist and states that are missing.
- Duplicate or conflicting patterns.
- Accessibility failures.
- Figma and code mismatches.

Use `templates/design-system-audit.md`.

## Step 2: Token architecture

Use three tiers:

| Tier | Purpose | Example |
| --- | --- | --- |
| Primitive | Raw values; never used directly in UI | `blue.600`, `space.4`, `radius.md` |
| Semantic | Meaningful roles; the main API | `color.action.primary`, `color.text.muted` |
| Component | Optional component-specific aliases | `button.primary.bg` |

### Naming

Use a consistent pattern:

```text
category.role.variant.state
```

Examples:

```text
color.text.primary
color.surface.raised
color.action.primary.hover
space.inset.md
radius.control
shadow.overlay
motion.duration.fast
motion.ease.out
```

### Token groups

- Color
- Typography
- Spacing
- Radius
- Border
- Shadow
- Motion
- Z-index
- Breakpoints
- Opacity

### Anti-generic foundations

Tokens can hide a lack of design thinking. A system that ships Inter as the only typeface, a violet-on-white gradient as the primary action, and one radius for every surface will make every product built on it look generated.

- Type tokens need a documented reason: construction, history, voice, or reading conditions. Inter, Roboto, Arial, Helvetica, and system stacks are not a neutral base; they are a choice to look like everyone else. If the brand mandates one, record the exception.
- Color tokens need a source and relationships. A violet, indigo, or purple gradient on white, or a blue-to-purple "AI" gradient, is a template, not a palette. Define at least one deliberate contrast pairing that carries meaning.
- Radius, border, and shadow must be role-based, not one value applied everywhere. Control, surface, and overlay need different treatment.
- Do not ship a card primitive whose only variant is the same radius and shadow.
- A component library is not a design direction. It is a grammar; the direction comes from the subject.

### Themes

Define themes by swapping semantic tokens, not by duplicating components:

```css
:root {
  --color-bg: oklch(98% 0.01 90);
  --color-text: oklch(20% 0.02 90);
  --color-action: oklch(55% 0.18 255);
}

[data-theme="dark"] {
  --color-bg: oklch(16% 0.02 90);
  --color-text: oklch(94% 0.01 90);
  --color-action: oklch(70% 0.14 255);
}
```

Use `color-scheme` for native controls and scrollbars. Test both themes with real content.

### Tailwind and CSS variables

A practical pattern:

```css
@theme {
  --color-background: var(--color-bg);
  --color-foreground: var(--color-text);
  --color-primary: var(--color-action);
  --radius-control: 0.5rem;
}
```

```html
<button class="bg-primary text-primary-foreground rounded-control">
  Save
</button>
```

Keep raw values in one place. Components consume semantic tokens, never primitives.

## Step 3: Component API

A component is a contract, not a screenshot.

Define:

| Field | Question |
| --- | --- |
| Purpose | What job does it do? |
| Anatomy | What are its parts? |
| Variants | What meaningful alternatives exist? |
| Sizes | What sizes are supported? |
| States | Default, hover, focus, active, disabled, loading, error, success |
| Slots | What content can be composed inside? |
| Controlled/uncontrolled | Who owns state? |
| Accessibility | Roles, labels, keyboard, focus |
| Responsive | How does it adapt? |
| Tokens | Which tokens does it consume? |
| Anti-patterns | When should it not be used? |

### Variants vs. props

- Use variants for visual or semantic alternatives: `primary`, `secondary`, `ghost`, `danger`.
- Use props for behavior and content: `disabled`, `loading`, `children`, `onClick`.
- Avoid a boolean explosion. If you have `isPrimary`, `isSecondary`, `isGhost`, use one `variant` prop.
- Prefer composition over a prop for every layout variation.

### Accessibility contract

Every component must define:

- Semantic element or role.
- Accessible name.
- Keyboard behavior.
- Focus management.
- Disabled behavior.
- Error announcement.
- Reduced-motion behavior.
- Touch target size.

## Step 4: Documentation

Each component page should include:

1. **Purpose** — what job it does.
2. **Anatomy** — labeled parts.
3. **Variants** — when to use each.
4. **Sizes** — when to use each.
5. **States** — visual examples.
6. **Do / Don't** — concrete examples.
7. **Accessibility** — keyboard, screen reader, contrast.
8. **Code** — copy-paste example.
9. **Tokens** — what it consumes.
10. **Related** — what to use instead.

Documentation that only shows the happy path is incomplete.

## Step 5: Figma/code parity

Keep design and code aligned:

- Use Figma variables for color, spacing, radius, and type.
- Name variables the same as code tokens.
- Use Code Connect to map Figma components to code components.
- Use the Figma MCP server to give agents components, styles, and variables as context.
- Generate a structured rules file from the codebase: token definitions, component inventory, naming conventions, and style hierarchy.
- Review drift on a schedule.

Figma’s MCP server sends contextual information like components, styles, and variables to an AI agent and can generate a structured rules file for token definitions, component libraries, style hierarchies, and naming conventions. Figma’s design-system agent uses real tokens, variables, and styles, not placeholders, and can generate components and audit consistency.

Sources: [Figma — Design Systems and AI](https://www.figma.com/blog/design-systems-ai-mcp), [Figma AI Design System Agent](https://www.figma.com/solutions/ai-design-system-agent)

## Step 6: Make it AI-readable

An AI agent needs a compact, explicit map of the system. Create:

```text
DESIGN.md
AGENTS.md
design/
  tokens.json
  components.json
  patterns.md
  anti-patterns.md
  examples/
```

### `DESIGN.md`

Include:

- Brand and product context.
- Design principles.
- Token names and meanings.
- Component inventory.
- Usage rules.
- Accessibility rules.
- Motion rules.
- Anti-patterns.
- Where to find examples.

### Component manifest

```json
{
  "button": {
    "path": "src/components/ui/button.tsx",
    "variants": ["primary", "secondary", "ghost", "danger"],
    "sizes": ["sm", "md", "lg"],
    "states": ["default", "hover", "focus", "active", "disabled", "loading"],
    "tokens": ["color.action.primary", "radius.control", "space.inset.md"],
    "accessibility": "Native button; visible focus; 44px min target"
  }
}
```

### Rules for agents

- Use existing components before creating new ones.
- Use semantic tokens, never raw hex or pixel values.
- Match the existing API and naming.
- Preserve keyboard and screen reader behavior.
- Add a reduced-motion path for animation.
- Add tests and a visual check.
- Do not introduce a new dependency without approval.

## Step 7: Governance

A design system without governance becomes a museum.

Define:

- **Owner:** who decides.
- **Contribution:** how to propose a component or token.
- **Review:** design and engineering sign-off.
- **Versioning:** semver for the package; changelog for behavior changes.
- **Deprecation:** notice, migration path, removal date.
- **Audit cadence:** quarterly token and component review.
- **Adoption metric:** percentage of screens using system components.
- **Exception process:** how to go off-system deliberately.

### Contribution checklist

- [ ] The pattern appears at least three times.
- [ ] Existing components cannot solve it.
- [ ] Anatomy and states are defined.
- [ ] Accessibility is covered.
- [ ] Tokens are used.
- [ ] Docs and examples exist.
- [ ] Tests and visual regression exist.
- [ ] Migration path is clear.

## Step 8: Tools

| Need | Options |
| --- | --- |
| Styling | CSS variables, Tailwind, CSS Modules, vanilla-extract |
| Primitives | Radix, React Aria, Headless UI |
| Copy-paste components | shadcn/ui |
| Documentation | Storybook, Ladle, custom docs |
| Visual regression | Chromatic, Playwright screenshots, Percy |
| Token pipeline | Style Dictionary, Tokens Studio, Figma variables |
| Figma/code bridge | Figma MCP, Code Connect |
| Icons | Lucide, Phosphor, custom set |

Choose the smallest stack that supports the team. A design system is not a tool purchase.

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Starting with components | Inconsistent foundations | Principles and tokens first |
| Too many tokens | Impossible to choose | Semantic roles, not every value |
| Raw values in components | Theme drift | Consume semantic tokens |
| Boolean prop explosion | Unmaintainable API | Variants and composition |
| Docs without do/don't | Misuse | Concrete examples |
| Figma and code drift | Visual bugs | Shared names, Code Connect, audits |
| No governance | Chaos or stagnation | Owner, contribution, deprecation |
| AI context missing | Generated UI bypasses the system | `DESIGN.md`, manifests, rules |
| Generic defaults baked into tokens | Every product on the system looks generated | Documented type and palette rationale; role-based radius and shadow |
| Accessibility as a variant | Broken by default | Accessible by default |

## Quality bar

- [ ] Principles are written.
- [ ] Type and palette tokens carry a documented rationale, not a default stack.
- [ ] Radius and shadow are role-based, not one value everywhere.
- [ ] Tokens have primitive, semantic, and optional component tiers.
- [ ] Themes swap semantic tokens.
- [ ] Components have variants, sizes, states, and accessibility contracts.
- [ ] Docs include anatomy, usage, do/don't, code, and accessibility.
- [ ] Figma and code use the same names.
- [ ] `DESIGN.md` and a component manifest exist.
- [ ] Governance and deprecation are defined.
- [ ] Visual regression and a11y checks run in CI.
- [ ] At least one real screen is built entirely from the system.

## Related skills

- `design-engineering` for the full workflow.
- `visual-ui-design` for the visual direction.
- `interaction-motion` for motion tokens.
- `frontend-craft` for implementation.
- `ai-design-workflow` for agent context.
- `design-critique` for system review.

## References

- `references/token-architecture.md` — token tiers, naming, themes, and examples.
- `templates/design-system-audit.md` — audit current state.
- `templates/component-spec.md` — component contract.
