# Reproducibility and Verification

Read this reference before finalizing every code-quality plan.

## Reproducibility checklist

For each in-scope project side, the plan must address:

- runtime/language version
- dependency/package manager
- lockfile or version-pinning strategy
- selected tool versions/constraints
- configuration source of truth
- one preferred command authority
- host/container/package-manager execution path
- VS Code/manual command parity
- GitHub CI command parity
- cache location and ownership when relevant
- generated and excluded paths

Prefer deterministic project-owned commands over developer-specific shell state.

## Static evidence vs runtime verification

Planning-time evidence comes from repository files. Runtime facts that cannot be
proven statically must be marked for the implementation-time baseline audit.

Examples of runtime-only checks:

- actual installed tool version
- command exit code
- current cache ownership/permissions
- whether the current codebase passes all checks
- whether container execution can write generated/cache files

## Verification requirements

Plan verification that demonstrates both correctness and stability:

1. formatter check passes without producing further changes
2. import-order check passes when enabled
3. linter passes according to approved strictness
4. type check passes when enabled
5. stylesheet lint passes when enabled
6. tests pass when they are part of the approved scope
7. repeated format/import/lint sequence remains stable with no fix-undo loop
8. approved VS Code Tasks call the intended project commands
9. approved save actions affect only intended file types/actions
10. GitHub CI uses the expected configuration, versions, and check commands

## Rollback

Every implementation step must state how to revert safely. Prefer small,
separable changes so tool configuration, editor integration, and GitHub CI can
be rolled back independently when possible.
