# Vuetify MCP Policy

The workspace codebase is the primary source of truth. MCP is a targeted documentation tool, not the first search mechanism.

Use Vuetify MCP only when at least one of these is true:

- The installed Vuetify version's API behavior is uncertain.
- A component prop, slot, event, theme setting, default, alias, accessibility behavior, or responsive utility must be verified.
- Repository examples conflict or are absent.
- The choice between custom implementation and a Vuetify standard feature depends on exact framework capability.

Do not use Vuetify MCP for:

- Backend work
- Generic TypeScript or Vue syntax
- Searching for project files
- Decisions already answered by repository code
- Every planning request by default

When MCP is used, report:

- The exact question sent to the tool
- The relevant result
- How it changed or confirmed the plan

If MCP is unavailable, continue with workspace evidence and explicitly mark the Vuetify detail for verification during implementation.
