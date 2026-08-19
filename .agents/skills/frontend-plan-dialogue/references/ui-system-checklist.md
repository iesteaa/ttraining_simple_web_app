# UI System Checklist

Before finalizing the plan, verify:

- Vuetify standard features are preferred over custom UI behavior.
- Existing theme, defaults, aliases, and responsive utilities were inspected.
- Similar pages and components were searched.
- Page-specific visual styling is not planned without a documented exception.
- Layout uses an existing layout component, or the plan explains why a reusable one must be created.
- Repeated UI is represented by a shared pattern or feature component.
- New design-system assets are domain-independent.
- MDI and the central icon registry are preferred for functional icons.
- Inline SVG and hard-coded SVG paths are not planned in pages or feature components.
- Decorative illustrations are separated from functional icons and placed in a stable frame.
- Icon and illustration slots reserve stable dimensions.
- Loading, empty, error, validation, permission, disabled, and long-content states are considered.
- Responsive behavior is explicit.
- Accessibility and keyboard behavior are included.
- Every planned new abstraction has a concrete responsibility and expected reuse scope.
