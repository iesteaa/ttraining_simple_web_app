---
applyTo: "src/**/*.vue,src/**/*.ts,src/**/*.css,src/**/*.scss"
---

# Frontend planning boundaries

When producing a frontend implementation plan:

- Inspect Vuetify theme, defaults, aliases, icons, design-system assets, and similar pages before proposing new UI.
- Prefer existing layout and pattern components.
- Do not plan page-local colors, spacing, typography, shape, shadow, or arbitrary Vuetify visual props.
- Prefer MDI through the central icon registry for functional icons.
- Do not plan inline SVG or hard-coded SVG paths in pages or feature components.
- Separate decorative illustrations from functional icons and reserve stable layout dimensions.
- Explain every proposed new shared abstraction and its intended reuse scope.
- Include loading, empty, error, validation, permission, responsive, and accessibility behavior where applicable.
