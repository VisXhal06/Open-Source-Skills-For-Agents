# Component Spec

## Name

[Component name.]

## Purpose

[What job it does and when to use it.]

## Anatomy

- Root:
- Label:
- Icon:
- Helper text:
- Error text:

## Variants

| Variant | Use when | Notes |
| --- | --- | --- |
|  |  |  |

## Sizes

| Size | Height | Padding | Type | Use when |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## States

| State | Visual | Behavior |
| --- | --- | --- |
| Default |  |  |
| Hover |  |  |
| Focus |  |  |
| Active |  |  |
| Disabled |  |  |
| Loading |  |  |
| Error |  |  |
| Success |  |  |

## API

```ts
type Props = {
  variant?: "primary" | "secondary" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
};
```

## Slots

-
-

## Accessibility

- Element/role:
- Accessible name:
- Keyboard:
- Focus:
- Disabled:
- Error announcement:
- Target size:
- Reduced motion:

## Tokens

| Token | Use |
| --- | --- |
|  |  |

## Responsive

- Mobile:
- Tablet:
- Desktop:

## Do

-
-

## Don't

-
-

## Code example

```tsx
<Button variant="primary" size="md">
  Save changes
</Button>
```

## Tests

- [ ] Unit
- [ ] Visual regression
- [ ] Keyboard
- [ ] Screen reader
- [ ] Dark mode
- [ ] Reduced motion
- [ ] Responsive

## Related

- Use instead:
- Related patterns:
