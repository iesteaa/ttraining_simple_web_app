# Final Plan Template

Use this structure after the user explicitly approves the consolidated
configuration. Omit sections that are not in scope.

```markdown
# Plan: Code Quality Setup

## Objective
[What will be standardized and why]

## Scope
- Backend: [included/excluded]
- Frontend: [included/excluded]

## Repository Evidence
### Backend
- Confirmed facts: [...] 
- Inconsistencies: [...]
- Runtime checks still required: [...]

### Frontend
- Confirmed facts: [...]
- Inconsistencies: [...]
- Runtime checks still required: [...]

## Confirmed User Decisions
### Backend
- Formatter: [...]
- Linter: [...]
- Import sorter: [...]
- Type checker: [...]
- Automatic save actions: [...]
- Manual execution: [...]
- VS Code Tasks: [...]
- GitHub CI: [...]
- Command authority: [...]

### Frontend
- Formatter: [...]
- Linter: [...]
- Import organization: [...]
- Type checker: [...]
- Stylesheet linter: [...]
- Automatic save actions: [...]
- Manual execution: [...]
- VS Code Tasks: [...]
- GitHub CI: [...]
- Command authority: [...]

## Responsibility Matrices
[one per in-scope side]

## Execution Matrices
[one per in-scope side]

## Reproducibility Policy
- Runtime/language versions: [...]
- Dependency/package-manager policy: [...]
- Lockfile/version policy: [...]
- Configuration source of truth: [...]
- Command authority: [...]
- Cache/ownership strategy: [...]
- Approved environment differences: [...]

## Conflict Resolution
- [conflict] -> [approved resolution]

## Planned Editor and VS Code Integration
- Automatic actions: [...]
- Manual tasks: [...]

## Planned GitHub CI Integration
- Backend checks: [...]
- Frontend checks: [...]
- Shared/root checks: [...]

## Planned File Changes
- `[path]` — [planned change and reason]

## Implementation Sequence
1. [step + dependency + expected outcome + verification + rollback]

## Verification
1. [specific command or behavior]

## Non-goals
- [...]

## Further Considerations
- [...]
```

The approved conversation plan is the implementation contract. Do not require a
repository plan file unless the user explicitly asks for one.
