# Frontend Checklist

## Structure

- [ ] Semantic landmarks: header, nav, main, footer.
- [ ] One `<h1>` per page; heading order is logical.
- [ ] Buttons are `<button>`; links are `<a href>`.
- [ ] Forms use `<label>`, `<fieldset>`, `<legend>` where appropriate.
- [ ] Lists use list elements.
- [ ] Tables use `<table>`, `<th>`, and captions.
- [ ] `<html lang>` is set.
- [ ] Skip link exists for long navigation.

## Layout

- [ ] CSS grid/flex used for layout.
- [ ] No horizontal scroll at 320px.
- [ ] Content max width is readable.
- [ ] Spacing uses tokens.
- [ ] Container queries used for component-level responsiveness.
- [ ] Fluid type with `clamp()` where appropriate.
- [ ] Images and embeds reserve space.
- [ ] Sticky elements do not obscure content.

## Type

- [ ] Body text is at least 16px.
- [ ] Line length is 45–75 characters.
- [ ] Line height is comfortable.
- [ ] Heading hierarchy is visual and semantic.
- [ ] Text is readable at 200% zoom.
- [ ] No all-caps long labels.
- [ ] No fake small caps or letter-spacing on body text.

## Color

- [ ] Semantic tokens used.
- [ ] Body contrast ≥ 4.5:1.
- [ ] Large text and UI contrast ≥ 3:1.
- [ ] Focus ring contrast ≥ 3:1.
- [ ] Color is not the only state signal.
- [ ] Dark mode is designed, not inverted.
- [ ] `color-scheme` is set.

## Interaction

- [ ] Hover states exist.
- [ ] Focus-visible states exist.
- [ ] Active/pressed states exist.
- [ ] Disabled states exist.
- [ ] Loading states exist.
- [ ] Empty states exist.
- [ ] Error states exist.
- [ ] Success states exist.
- [ ] Touch targets are at least 24×24 (44×44 recommended).
- [ ] Hit areas do not move during animation.

## Keyboard

- [ ] Every interactive element is reachable.
- [ ] Tab order is logical.
- [ ] Focus is visible.
- [ ] Escape closes overlays.
- [ ] Focus is trapped in modals.
- [ ] Focus returns to the trigger.
- [ ] Arrow keys work in menus, tabs, and listboxes.
- [ ] No keyboard traps.

## Screen reader

- [ ] Images have alt text; decorative images are empty alt.
- [ ] Icons have accessible names or are hidden.
- [ ] Form errors are announced.
- [ ] Dynamic content uses `aria-live` appropriately.
- [ ] Dialog has a name.
- [ ] Buttons have clear names.
- [ ] Links describe their destination.

## Motion

- [ ] Every animation has a purpose.
- [ ] Reduced motion is respected.
- [ ] No flashing above three times per second.
- [ ] No scroll-jacking.
- [ ] Animation uses transform/opacity.
- [ ] Offscreen animation is paused.
- [ ] Animation does not block input.

## Performance

- [ ] LCP ≤ 2.5 s.
- [ ] INP ≤ 200 ms.
- [ ] CLS ≤ 0.1.
- [ ] Hero image is optimized and prioritized.
- [ ] Fonts are subset and preloaded.
- [ ] JS is code-split.
- [ ] Client components are minimal.
- [ ] Third parties are deferred or removed.
- [ ] Long lists are virtualized.
- [ ] Bundle size is reviewed.

## Responsive

- [ ] 320px.
- [ ] 375px.
- [ ] 768px.
- [ ] 1024px.
- [ ] 1440px.
- [ ] 1920px.
- [ ] Landscape mobile.
- [ ] 200% zoom.
- [ ] Large text.

## Cross-browser

- [ ] Chrome.
- [ ] Safari.
- [ ] Firefox.
- [ ] Edge.
- [ ] iOS Safari.
- [ ] Android Chrome.

## Content

- [ ] Real copy, not lorem ipsum.
- [ ] Long content tested.
- [ ] Empty state copy is useful.
- [ ] Error copy explains what happened and how to fix it.
- [ ] CTA labels are specific.
- [ ] No placeholder links.

## Testing

- [ ] Unit tests.
- [ ] Integration tests.
- [ ] Visual regression.
- [ ] axe or equivalent.
- [ ] Lighthouse.
- [ ] Keyboard walkthrough.
- [ ] Screen reader walkthrough.
- [ ] Real device test.
