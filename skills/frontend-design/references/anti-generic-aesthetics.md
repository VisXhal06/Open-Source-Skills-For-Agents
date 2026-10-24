# Anti-Generic Aesthetics Gate

This is a gate, not a mood. Generic AI aesthetics are rejected as defaults even when they are competently executed, because competence is not the same as design.

The rule: **never use an overused type stack, a clichéd palette, a predictable layout, or a cookie-cutter component pattern without a subject-specific reason.** Recoloring a template does not make it specific. Changing the border radius does not make it a direction.

## What is banned as a default

A banned choice may ship only when the brief, the brand, or the existing design system explicitly requires it. When that happens, record the exception and follow the requirement exactly. An exception is not a preference.

### Typography

| Banned as a default | Why it reads generated | Replace with |
| --- | --- | --- |
| Inter | The default face of every AI-generated SaaS page; visually neutral to the point of anonymity | A face chosen for the subject's construction, history, or voice |
| Roboto | Android's default, used as a stand-in for "modern" | A face with a reason to exist in this product |
| Arial, Helvetica | The fallback stack, not a decision | A deliberate grotesque, humanist, serif, or display face |
| `system-ui`, `-apple-system`, `Segoe UI`, `San Francisco` | The browser's choice, not the designer's | A licensed or open face that carries the brief |
| Poppins, Montserrat, Open Sans, Lato | The 2018 template stack; rounded geometry with no point of view | A face that fits the industry, material, or audience |
| One family for everything when the subject demands contrast | Convenience mistaken for restraint | One family used with range, or two clearly distinct families |

Do not substitute a novelty face for legibility. The replacement must still work at body size, at 200% zoom, and with long content.

### Color

| Banned as a default | Why it reads generated | Replace with |
| --- | --- | --- |
| Violet, indigo, or purple gradients on white or near-white | The "AI product" cliché; the gradient does no semantic work | A palette derived from the subject's materials, place, artifacts, or brand |
| Blue-to-purple "AI" gradients | Signals "tech" without saying which tech or why | A controlled palette with one purposeful accent |
| Gradient text on a headline | Decoration standing in for hierarchy | Weight, scale, and space; color only if it carries meaning |
| Pastel gradient mesh or blurred blobs behind a hero | Hides a weak composition | A real image, a strong type treatment, or deliberate empty space |
| Glass cards floating on a gradient | Trend stack with poor contrast and no content logic | Opaque surfaces with role-based depth, or real translucency with a reason |
| Near-black plus one acid-green or vermilion accent | The second most common generated palette | A palette with a documented source and more than one relationship |
| Cream plus high-contrast serif plus terracotta | A recognizable template, not a neutral choice | A direction derived from the subject, not from a trend |

A palette needs 4–6 named core values and a stated source. "Looks clean" and "feels modern" are not sources.

### Layout

| Banned as a default | Why it reads generated | Replace with |
| --- | --- | --- |
| Centered hero: eyebrow badge, two-line headline, grey subhead, two buttons, gradient blob | The default landing-page skeleton, independent of product | A composition that opens with the most characteristic thing in the subject's world |
| Three identical feature cards in a row | Content forced into equal containers | A structure that gives each idea the weight it earns |
| Logo cloud of grey wordmarks | Social proof as decoration | Specific evidence, or no logo section |
| Three testimonial cards with the same avatar treatment | Filler content in a predictable shape | One real story, or a different proof format |
| Three-tier pricing with the middle card highlighted | The SaaS pricing default | Pricing structured around the actual decision |
| Bento grid of identical tiles | Trend applied without hierarchy | Varied scale and one clear focal cell, if bento fits at all |
| Dashboard mockup floating in the hero | Product screenshot as a substitute for a promise | A real product moment, a live demo, or a specific claim |
| Every section wrapped in a rounded card | Containers instead of composition | Space, rules, and type to create structure |
| Sticky blurred nav with a pill CTA | Template chrome | Navigation shaped by the product's actual information architecture |

### Components

| Banned as a default | Why it reads generated | Replace with |
| --- | --- | --- |
| A pill badge above every heading | Eyebrow label as a nervous tic | A label only where it encodes real information |
| One border-radius on every surface | No hierarchy between control, card, and overlay | Radius by role: control, surface, overlay |
| One soft shadow under every card | Depth without meaning | Elevation only where layering means something |
| Icon in a rounded square for every feature | The feature-grid kit | Icons only where they aid recognition; vary treatment by role |
| Gradient-border cards | Trend stack; often inaccessible | A border or surface that expresses hierarchy |
| Hover-lift on every card | Motion as default polish | Motion that answers an action or shows a change |
| Identical cards for different content types | Container-first thinking | A layout that responds to the content |

### Motion

| Banned as a default | Why it reads generated | Replace with |
| --- | --- | --- |
| Fade-and-slide-up on every section | The default scroll-reveal kit | One orchestrated moment, or motion tied to an event |
| Staggered reveal on every list | Animation applied to content it does not explain | Stagger only when sequence matters |
| Hover scale on every card | Decorative feedback on non-actions | Feedback only on interactive elements |
| Looping ambient gradient or blob | Motion with no message | Stillness, or motion with a purpose |
| Cursor-following blob or magnetic everything | Novelty in place of interaction design | One signature interaction that fits the subject |

### Imagery and copy

- Generic 3D blobs, abstract AI orbs, and stock "diverse team" photography are defaults. Use real artifacts, real places, real people, or no image.
- "Build faster, ship smarter", "AI-powered", "supercharge", "seamless", "unlock", and "the future of work" are banned as unexamined copy. Every claim must be specific and checkable.
- Decorative numbers (`01 / 02 / 03`) are banned unless the content is genuinely a sequence.

## Exceptions

A banned default may be used when:

1. The brand already owns it and changing it would break recognition.
2. The existing design system mandates it and this task is not a redesign.
3. The brief explicitly asks for that look, including a deliberate parody or period reference.
4. A platform constraint leaves no alternative, such as a system font in a native shell.

Write the exception in the design record. "I like it" is not an exception. An exception for one element does not license the rest of the page.

## Required design record

Before implementation, write six lines. If a line cannot be written specifically, the direction is not ready.

```text
Direction: <name> — <why it belongs to this subject>
Type: <face> — <what its construction, history, or voice contributes>
Palette: <source> — <4–6 core values>
Layout: <what the structure encodes> — <what it deliberately breaks>
Signature: <the one element that could not move to another product>
Rejected: <the specific defaults this brief refuses>
```

## How to find a specific direction

Mine the subject, not the trend:

1. **Material:** what is it made of, printed on, grown in, or shipped in? Paper, ink, metal, soil, fabric, glass, circuitry.
2. **Place:** where does it live? A city, a workshop, a landscape, a kitchen, a trading floor. Use the light, signage, and texture of that place.
3. **Artifact:** what objects does the audience already use? Tickets, ledgers, manuals, labels, instruments, maps.
4. **Vocabulary:** what words does the audience use that a generic SaaS page would never use?
5. **Ritual:** what do people actually do with it? Compare, annotate, scan, browse, decide, wait, hand off.

A direction is specific when it could not be swapped into an unrelated product without becoming wrong.

## Review rubric

Score each axis **specific**, **weak**, or **banned default**:

| Axis | Specific | Weak | Banned default |
| --- | --- | --- | --- |
| Type | Chosen for this subject, with a reason | Neutral but not a named default | Inter, Roboto, Arial, Helvetica, system stack, template stack |
| Color | Source named; roles clear; one accent | Pleasant but arbitrary | Purple-on-white gradient, blue-purple AI gradient, gradient text |
| Layout | Structure encodes the content | Conventional but functional | Centered hero kit, three identical cards, pricing trio, identical bento |
| Components | Role-based shape and depth | Some variation | One radius/shadow, pill every heading, icon-square kit |
| Motion | One purposeful moment | Restrained but generic | Fade-slide everywhere, hover-lift everywhere, ambient loop |
| Copy | Specific and checkable | Plain but honest | "Build faster, ship smarter" and its relatives |

Any **banned default** on the axes that define the first impression is a **blocker**. A banned default in a secondary element is a **major** finding. It is never a nit.

## Evidence

- A rendered page or screenshot at 320, 768, and 1440 px.
- The design record, with the rejected defaults named.
- For a review, the specific pattern and the replacement, not "it looks AI-generated".
- If the work is in an existing project, evidence that the choice matches that project's system or a documented exception.

## Self-check

- Could this page be dropped into another product with a logo swap? If yes, it is generic.
- Is the typeface on the banned list, or chosen for a reason I can say in one sentence?
- Does the palette have a source outside "modern" and "clean"?
- Is the layout the content's shape, or a template the content was poured into?
- Is there one element I could not move to another project?
- Did I reject something specific, or only decorate the default?
- Would a senior designer be able to tell what this product is from the design alone?
