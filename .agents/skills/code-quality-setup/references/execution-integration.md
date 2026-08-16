# Execution and Integration Guidance

Use this reference when deciding how selected quality tools are run.

Treat the following as independent decisions.

## 1. Automatic editor actions

Ask what should happen when a relevant file is saved:

- no automatic actions
- format only
- format and organize imports
- format, organize imports, and apply explicitly approved safe lint fixes
- keep existing save actions

Rules:

- do not run the full test suite on every save by default
- do not run a project-wide type check on every save by default
- do not enable automatic lint fixes unless the user approves them
- configure per-language default formatters when backend/frontend use different tools
- preserve editor-neutral behavior when the team does not standardize on VS Code

## 2. Manual execution

Ask how developers should intentionally run quality checks:

- project/package-manager/task-runner commands
- VS Code Tasks
- both, with VS Code Tasks delegating to the shared project command
- keep existing workflow

If VS Code Tasks are selected, ask whether to create:

- individual tasks per selected responsibility
- one combined `Code Quality: Check All` task
- individual tasks plus `Check All`
- keep existing tasks

Prefer Tasks that call a shared project command rather than duplicating complex
tool flags in `tasks.json`.

Suggested labels, only when relevant:

- `Backend: Format`, `Backend: Lint`, `Backend: Type Check`, `Backend: Code Quality Check All`
- `Frontend: Format`, `Frontend: Lint`, `Frontend: Type Check`, `Frontend: Code Quality Check All`
- optional root `Code Quality: Check All` for both sides

## 3. GitHub-side enforcement

Use GitHub Actions / CI as the quality gate when the user chooses GitHub-side
enforcement.

Ask whether GitHub CI should use:

- full parity with approved local check commands
- selected critical checks only
- stricter checks than local
- no CI integration yet
- keep existing CI behavior

Prefer check-only CI commands. CI should fail on violations instead of silently
modifying source files.

Plan the workflow's:

- triggers and path scope
- backend/frontend job split or combination
- dependency setup and lockfile use
- cache strategy when safe
- exact shared check commands
- configuration/version parity with local workflows

## GitHub CLI (`gh`)

Treat `gh` as an optional operational interface for viewing or manually
triggering GitHub workflows, not as the formatter/linter execution engine.
Do not replace reproducible GitHub Actions jobs with ad-hoc `gh` commands unless
the user explicitly requests that workflow.

## Execution matrix

Create one matrix per project side:

| Responsibility | Tool | On Save | Manual Command | VS Code Task | GitHub CI |
|---|---|---:|---:|---:|---:|
| Formatting | [tool] | | | | |
| Import sorting | [tool] | | | | |
| Linting | [tool] | | | | |
| Type checking | [tool] | no | | | |
| Stylesheet linting | [tool/n-a] | | | | |

Do not enable every trigger by default. Follow user preference and use the
smallest workflow that satisfies the requested quality guarantees.
