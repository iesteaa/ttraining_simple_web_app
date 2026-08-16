---
name: code-quality-setup
description: >-
  Plan reusable and reproducible code-quality setup for backend, frontend, or
  both. Use when selecting, migrating, or standardizing formatter, linter,
  import sorting, type checking, VS Code Format on Save, VS Code Tasks, project
  commands, and GitHub CI. Discover the repository first, let the user choose
  relevant tools and execution behavior, detect conflicts, and produce a
  verifiable implementation plan without implementing changes.
---

# Code Quality Setup Planning

Use this skill as the reusable procedure behind a read-only code-quality
planning agent.

## Scope

Plan only the quality responsibilities the project actually needs:

- formatting
- general linting
- import sorting / organize imports
- type checking
- optional stylesheet linting for frontend projects
- automatic editor actions
- manual project commands and VS Code Tasks
- GitHub CI enforcement

Do not force every responsibility or integration on every project. `None` and
`Keep existing` are valid outcomes when supported by repository evidence and
user preference.

## Workflow

### 1. Classify the project scope

Determine whether the request covers:

- backend only
- frontend only
- backend and frontend separately

Detect the ecosystem and active dependency/package workflow before asking for
tool choices.

### 2. Discover repository evidence

Use read-only exploration. Inspect active configuration, dependency files,
lockfiles, project scripts, VS Code settings/tasks, container/task-runner files,
and GitHub workflows.

Separate findings into:

- **Confirmed facts** — proven by repository files
- **Inconsistencies** — version, command, ownership, or workflow drift
- **Unverified assumptions / runtime checks** — facts that require execution later

Do not claim runtime versions, exit codes, cache ownership, or actual command
results unless they were observed.

### 3. Load only relevant ecosystem guidance

- For a Python backend, read `references/backend-python.md`.
- For a JavaScript/TypeScript frontend, read `references/frontend-js-ts.md`.
- For editor/manual/GitHub execution choices, read `references/execution-integration.md`.
- Before finalizing any plan, read `references/reproducibility-verification.md`.
- When producing the final output, read `references/plan-template.md`.

If the repository uses an ecosystem not covered by these references, preserve
existing tools where possible and explicitly identify unsupported knowledge
instead of inventing tool-specific rules.

### 4. Let the user choose tools per project side

Use repository evidence to narrow the choices. Do not show an irrelevant tool
catalog.

For every in-scope side, establish one clear owner for each selected
responsibility:

| Responsibility | Owner |
|---|---|
| Formatting | one tool or none |
| Import sorting | one tool or none |
| General linting | one tool or none |
| Type checking | one tool or none |
| Stylesheet linting | one frontend tool or n/a |

Preserve existing tools when they are already appropriate. If the user chooses
`Keep existing` but no mechanism exists, ask again instead of silently choosing
a default.

### 5. Ask execution preferences independently

Do not treat Format on Save, VS Code Tasks, and GitHub CI as mutually exclusive.
Ask three independent decisions:

1. **Automatic editor actions** — what should happen on save?
2. **Manual execution** — how should developers run checks intentionally?
3. **GitHub CI** — which checks should be enforced on push/pull request?

Use `references/execution-integration.md` for the decision model.

### 6. Define reproducibility

For every in-scope project side, define:

- runtime/language version policy
- dependency/package-manager and lockfile strategy
- tool version policy
- configuration source of truth
- command authority
- host/container/package-manager execution path
- editor/manual command parity
- GitHub CI command parity
- cache location/ownership when relevant
- generated/excluded paths

Prefer one stable command authority per side. Document intentional environment
differences instead of claiming false parity.

### 7. Review conflicts

Before approval, check at least:

- duplicate responsibility ownership
- formatter/linter style overlap
- line-length conflicts
- import-sorting overlap
- editor extension/save-action conflicts
- generated-code exclusions
- host/container cache or ownership problems
- lockfile/version drift
- local/VS Code/GitHub command drift

Use ecosystem references for known conflict areas, but treat the repository's
active versions and configuration as the source of truth.

### 8. Confirm before planning implementation

Show one consolidated configuration summary covering each in-scope side:

- selected responsibilities and tools
- automatic save actions
- manual command entry point
- VS Code Tasks
- GitHub CI
- command authority
- version/lockfile policy
- scope/non-goals

Request explicit approval. Do not generate the final implementation plan before
approval.

### 9. Produce a verifiable plan

Use `references/plan-template.md`.

Every planned change must identify:

- affected file(s)
- dependency/order
- expected outcome
- verification
- rollback

The plan must instruct the implementation agent to verify any runtime facts that
were not observable during planning.

## Planning boundaries

- Produce a plan, not implementation.
- Do not edit files or run mutating commands.
- Do not make GitHub CI modify source by default; prefer check-only enforcement.
- Do not enable automatic actions without explicit user approval.
- Do not run full tests or project-wide type checking on every save by default.
- Do not overwrite unrelated VS Code Tasks, settings, scripts, or workflows.
- Do not combine unrelated cleanup or dependency modernization into the plan
  without user approval.
