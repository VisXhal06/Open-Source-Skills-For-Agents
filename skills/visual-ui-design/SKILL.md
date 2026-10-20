---
name: visual-ui-design
description: "Use when designing the visual layer of a product or page: layout, typography, color, spacing, hierarchy, responsive behavior, dark mode, visual style, or making an interface feel modern, distinctive, and polished."
license: MIT
compatibility: opencode
metadata:
  version: "1.0.0"
---

# Visual UI Design

Design the surface so the product is clear, distinctive, and usable. This skill covers layout, typography, color, spacing, hierarchy, responsive behavior, dark mode, and visual style selection.

## Suite integration

Part of the design-engineering suite. `design-engineering` can load this skill automatically when the user asks to design a UI or make it look better. Direct invocation works too. If `design-research` produced a direction, use its principles and references as input.

## The visual system

A visual system is not a moodboard. It is a set of decisions that can be applied consistently:

| Layer | Decision |
| --- | --- |
| Concept | One sentence that captures the idea |
| Hierarchy | What the eye sees first, second, third |
| Grid | Columns, gutters, margins, breakpoints |
| Spacing | A scale, not arbitrary values |
| Typography | Typefaces, roles, scale, line height, measure |
| Color | Semantic roles, palette, contrast, themes |
| Imagery | Photography, illustration, 3D, texture, or none |
| Shape | Radii, borders, shadows, density |
| Motion | One signature moment and its purpose |
| States | Empty, loading, error, success, disabled, focus, hover, active |

## Step 1: Read the brief

Extract:

- Audience and context of use.
- Job to be done.
- Three feeling adjectives.
- Content type and density.
- Brand constraints.
- Accessibility and performance constraints.
- Anti-goals.

If the brief is missing, load `design-research` or write a one-page brief first.

## Step 2: Choose a direction

Use the brief to choose a direction, not a trend. The table below is a starting point, not a menu.

| Direction | Fits when | Risks | Key moves |
| --- | --- | --- | --- |
| **Editorial** | Content, publishing, culture, premium consumer | Can feel slow or dense | Strong type hierarchy, generous margins, asymmetry, real imagery |
| **Swiss / international** | Clarity, systems, professional tools | Can feel cold or generic | Grid, sans-serif, left alignment, restrained color, strong spacing |
| **Minimal** | Focus, speed, premium utility | Can feel empty or unfinished | Whitespace, few colors, one accent, precise type |
| **Warm humanist** | Health, education, community, consumer | Can feel soft or untrustworthy | Rounded forms, warm neutrals, organic shapes, friendly type |
| **Technical / utilitarian** | Developer tools, data, infrastructure | Can feel hostile or cluttered | Monospace accents, dense grids, clear states, restrained motion |
| **Brutalist / neo-brutalist** | Culture, fashion, portfolios, bold brands | Can hurt usability and accessibility | Raw type, hard borders, high contrast, deliberate imperfection |
| **Glass / tactile** | Premium, spatial, media, AI products | Can hurt contrast and performance | Translucency, layered depth, soft gradients, precise blur |
| **Bento** | Feature tours, dashboards, product marketing | Can become a grid of identical cards | Modular cells, varied scale, one hero cell, clear hierarchy |
| **Maximalist / collage** | Fashion, art, youth, entertainment | Can overwhelm and slow down | Layering, texture, mixed type, controlled chaos |
| **Retrofuturist** | Games, music, experimental brands | Can date quickly | Chrome, neon, pixel, sci-fi references, strong motion |
| **Organic / anti-grid** | Wellness, sustainability, creative tools | Can break responsiveness and CLS | Fluid shapes, soft gradients, asymmetric flow, calm motion |

Do not combine five directions. Pick one primary direction and one accent influence.

## The anti-generic gate

The direction table is a vocabulary, not a preset menu. "Swiss" does not mean Inter on white; "technical" does not mean near-black plus acid green; "glass" does not mean purple-gradient cards. A direction earns its name through specific type, color, layout, and motion decisions.

Banned as defaults:

- **Type:** Inter, Roboto, Arial, Helvetica, and `system-ui` / `-apple-system` / `Segoe UI` stacks; the Poppins / Montserrat / Open Sans / Lato template stack.
- **Color:** violet, indigo, or purple gradients on white or near-white; blue-to-purple "AI" gradients; gradient text; pastel mesh or blurred-blob backgrounds; glass cards on a gradient.
- **Layout:** the centered eyebrow-headline-two-buttons hero with a gradient blob; three identical feature cards; logo cloud; testimonial trio; pricing trio with a highlighted middle card; identical bento tiles; floating dashboard mockup; every section in a rounded card.
- **Components:** a pill badge above every heading; one radius and one shadow on every surface; icon-in-rounded-square for every feature; gradient-border cards; hover-lift on every card.
- **Motion:** fade-and-slide-up on every section; stagger on every list; hover scale on every card; looping ambient gradient.
- **Copy:** "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock" without a specific claim.

Before implementation, write the six-line design record from `frontend-design` (`references/anti-generic-aesthetics.md`): direction, type rationale, palette source, layout logic, signature element, rejected defaults. A banned default that defines the first impression is a blocker; in a secondary element it is a major finding. Recoloring is not a replacement.

## Step 3: Define hierarchy

Hierarchy is the most important visual decision. Before color, before decoration, answer:

1. What is the one thing on this screen?
2. What supports it?
3. What is secondary?
4. What can disappear?

Use size, weight, contrast, space, and position — in that order. Color is a weak hierarchy tool when everything is colored.

### Above the fold

The first screen should answer:

- What is this?
- Who is it for?
- Why should I care?
- What do I do next?

Do not open with a generic big number, a gradient blob, or a floating dashboard card unless the content genuinely calls for it.

## Step 4: Typography

### Type system

Define:

| Role | Size | Weight | Line height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| Display |  |  |  |  | Hero, one per page |
| H1 |  |  |  |  | Page title |
| H2 |  |  |  |  | Section |
| H3 |  |  |  |  | Subsection |
| Body |  |  |  |  | Reading |
| Small |  |  |  |  | Metadata |
| Label |  |  |  |  | Controls, captions |

### Rules

- Use one family, or two that are clearly distinct. Three is usually a crowd.
- Do not default to Inter, Roboto, Arial, Helvetica, a `system-ui` stack, or the Poppins / Montserrat / Open Sans / Lato stack. If the brand mandates one, record the exception; otherwise choose a face for this subject.
- Name why the face fits: construction, history, voice, or reading conditions. "Clean and modern" is not a reason.
- Body line length: 45–75 characters. Serif can go slightly longer.
- Body line height: roughly 1.4–1.7, depending on typeface and size.
- Use a modular scale, but adjust optically. A 1.25 ratio is a safe start.
- Avoid all-caps for long labels. Use sentence case for controls.
- Do not accent one word in a headline with italic, bold, or color just to add interest. It is a common generated-design tell.
- Variable fonts can carry weight, width, and optical size, but test rendering and performance.
- Check text at 200% zoom and with increased line spacing.

### Type as voice

- Editorial: high contrast, dramatic scale, generous leading.
- Technical: compact, monospace accents, tight hierarchy.
- Warm: rounded terminals, softer contrast, comfortable leading.
- Luxury: restrained scale, wide margins, precise spacing, few weights.

## Step 5: Color

### Color roles

Define semantic roles, not raw colors:

| Role | Purpose |
| --- | --- |
| `background` | Page base |
| `surface` | Cards, panels |
| `surface-raised` | Modals, popovers |
| `text` | Primary text |
| `text-muted` | Secondary text |
| `border` | Dividers, inputs |
| `primary` | Main action |
| `primary-foreground` | Text on primary |
| `success` / `warning` / `danger` / `info` | Feedback |
| `focus` | Keyboard focus ring |

### Rules

- Start with 4–6 core values, then derive tints and shades.
- Do not use a violet, indigo, or purple gradient on white, or a blue-to-purple "AI" gradient. Build the palette from a named source outside the trend: material, place, artifact, or brand.
- A palette needs relationships, not one hue with tints. Define at least one deliberate warm/cool or high/low contrast pairing that does semantic work.
- Body text needs at least 4.5:1 contrast; large text at least 3:1.
- Do not use color alone to communicate state. Pair with text, icon, or shape.
- Reserve the most saturated color for the primary action or one signal.
- Test dark mode separately; do not simply invert.
- Check color blindness with a simulator, not just a contrast checker.
- Use `color-scheme` and semantic tokens so system preference works.

## Step 6: Layout and spacing

### Spacing scale

Use a consistent scale, for example:

`4, 8, 12, 16, 24, 32, 48, 64, 96, 128`

Use smaller steps inside components, larger steps between sections. Avoid arbitrary `13px` and `27px` unless optically necessary.

### Layout

- Choose a grid: 4, 8, or 12 columns. Use it, then break it deliberately.
- Define max content width. Long lines are hard to read.
- Use whitespace to group and separate. Space is hierarchy.
- On mobile, design the actual mobile hierarchy; do not squeeze desktop.
- Use container queries when a component's layout depends on its container, not the viewport.
- Reserve space for images, ads, and dynamic content to prevent CLS.
- Test at 320px, 768px, 1024px, and 1440px at minimum.

### Density

- Consumer: generous spacing, fewer items per screen.
- Professional tool: higher density, but clear grouping and alignment.
- Data-heavy: use tables, sticky headers, and progressive disclosure, not cards everywhere.

## Step 7: Shape, depth, and detail

- **Radii:** choose a small set (e.g., 4, 8, 12, 999). Do not use the same radius on everything.
- **Borders:** 1px hairlines for structure; avoid borders when space can do the job.
- **Shadows:** one or two elevation levels, not a shadow on every card.
- **Gradients:** use for atmosphere or brand, not to hide weak layout.
- **Texture:** subtle noise, paper, or grain can add warmth; keep it performant.
- **Icons:** one family, consistent stroke, optically aligned. Do not mix filled and outline arbitrarily.
- **Imagery:** real content beats stock. If using illustration, define a consistent style.
- **Empty space:** a deliberate void is a design element, not a failure.

## Step 8: States

A screen is not designed until every state exists:

- Default
- Hover
- Focus-visible
- Active/pressed
- Disabled
- Loading
- Empty
- Error
- Success
- Partial/unknown
- Long content
- No permission
- Offline

Design the state, not just the happy path. Most perceived quality comes from these.

## Step 9: Responsive and dark mode

### Responsive

- Mobile-first CSS, but design the mobile composition, not just the stack.
- Use fluid type and spacing with `clamp()` where appropriate.
- Avoid horizontal scroll except for deliberate carousels or tables.
- Keep touch targets at least 24×24 CSS px (44×44 recommended).
- Test landscape, zoom, and large text.

### Dark mode

- Use semantic tokens.
- Avoid pure black and pure white; use near-black and off-white.
- Reduce saturation for large surfaces; increase contrast for text.
- Check shadows and borders; they often disappear.
- Respect `prefers-color-scheme` and offer a manual toggle.

## Step 10: Critique the direction

Before building, review:

- Is the hierarchy obvious in three seconds?
- Is the direction specific to the subject, or could it be any SaaS?
- Could this page be swapped into another product with only a logo change? If yes, the direction is generic.
- Is the typeface chosen for a reason, or inherited from a template stack?
- Which specific default did we reject, and can we name it?
- Does it work with real content?
- Does it survive mobile and dark mode?
- Is the type readable at 200% zoom?
- Is the palette accessible?
- Is there one memorable moment, or five competing ones?
- What can be removed?

## Common mistakes

| Mistake | Consequence | Fix |
| --- | --- | --- |
| Trend collage | Generic, dated, incoherent | One primary direction |
| Default type stack (Inter, Roboto, Arial, system) | Anonymous, reads as generated | Face chosen for the subject, with a reason |
| Purple-on-white or blue-purple gradient | The AI-product cliché | Palette with a documented source |
| Centered badge-headline-two-buttons hero | Template skeleton, not a composition | Open with the subject's most characteristic thing |
| Same radius and shadow everywhere | Flat, templated feel | Vary shape by role |
| Decorative gradients | Hides weak layout | Fix hierarchy, then add atmosphere |
| All-caps labels | Hard to scan | Sentence case |
| Tiny body text | Unreadable on mobile | 16px minimum, test zoom |
| Desktop-only layout | Broken mobile | Design mobile composition |
| No states | Feels unfinished | Design every state |
| Dark mode by inversion | Harsh, illegible | Design dark mode separately |

## Quality bar

- [ ] One primary direction, with a one-sentence concept.
- [ ] Anti-generic gate passed: no banned type stack, palette, layout, or component kit.
- [ ] Type, palette, and layout each have a stated rationale tied to the subject.
- [ ] Hierarchy is obvious.
- [ ] Type scale and measure are defined.
- [ ] Color roles are semantic and accessible.
- [ ] Spacing uses a scale.
- [ ] Mobile, tablet, and desktop are designed.
- [ ] Dark mode is designed.
- [ ] All states exist.
- [ ] Real content is used.
- [ ] Keyboard focus is visible.
- [ ] The direction is specific to the subject.

## Related skills

- `design-engineering` for the full workflow.
- `design-research` for the brief and direction.
- `interaction-motion` for states and animation.
- `design-systems` for tokens and components.
- `frontend-craft` for implementation.
- `design-critique` for review.
- `frontend-design` for distinctive aesthetic risk.

## References

- `references/style-directions.md` — deeper notes on each visual direction.
- `templates/style-tile.md` — one-page direction.
- `templates/ui-spec.md` — visual and component specification.
