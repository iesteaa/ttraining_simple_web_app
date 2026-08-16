# JavaScript / TypeScript Frontend Guidance

Load this reference only when a JavaScript/TypeScript frontend is in scope.

## Discovery

Inspect relevant active files such as:

- `package.json`
- npm/pnpm/Yarn/Bun lockfiles
- `eslint.config.*` or `.eslintrc*`
- `.prettierrc*` or `prettier.config.*`
- `biome.json` / `biome.jsonc`
- `tsconfig*.json`
- `stylelint.config.*` when relevant
- framework scripts and config
- frontend VS Code Tasks/settings
- frontend GitHub workflow commands

## Tool choices

Offer only choices relevant to the detected framework and current project.

| Responsibility | Common choices |
|---|---|
| Formatting | Prettier, Biome formatter, keep existing, none |
| General linting | ESLint, Biome linter, keep existing, none |
| Import organization | existing ESLint/plugin mechanism, Biome organize imports, project mechanism, none |
| Type checking | `tsc --noEmit`, `vue-tsc` when appropriate, framework/project command, none |
| Stylesheet linting | Stylelint, existing mechanism, none |

## Conflict areas to review

- Prettier vs ESLint stylistic/formatting rules
- Biome used alongside Prettier or ESLint with overlapping ownership
- multiple import-sorting mechanisms
- framework-specific type checker vs plain `tsc`
- VS Code default formatter conflicts by language
- save actions that duplicate project scripts or apply unsafe fixes

Assign one clear owner to each responsibility. If separate tools coexist, state
why they do not overlap.

## Command authority examples

Prefer package-manager scripts backed by the project's lockfile when practical:

- `npm run ...`
- `pnpm ...`
- `yarn ...`
- `bun run ...`

VS Code Tasks and GitHub CI should reuse the same project scripts when that
reduces duplication and drift.
