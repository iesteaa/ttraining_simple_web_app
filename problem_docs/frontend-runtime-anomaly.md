# Frontend Runtime Anomaly with Dev Container State

**Date:** 2026-08-14
**Status:** Partially resolved, with Firefox anomaly still unresolved

## Problem

The frontend showed abnormal behavior that depends on whether the VS Code dev container is running.

Observed symptom:

- the localhost frontend page behaves normally when the dev container is stopped and `docker compose up` is run from the local VS Code environment;
- when the dev container is running, local code edits do not make the localhost frontend page behave normally and the page can stay in a loading state;
- Google Chrome behaves normally in the working case, while Mozilla Firefox still shows abnormal behavior in the failing case.

## What Was Observed

1. When the dev container was not running, `docker compose up` from the local VS Code environment behaved normally.
2. When the dev container was running, local file edits did not consistently produce normal frontend behavior in the browser.
3. The frontend app itself is minimal and does not contain loading-state logic that would explain a permanent loading screen.
4. Chrome worked normally after the runtime configuration was adjusted.
5. Firefox remained abnormal even after the same runtime changes were applied.

## Working Hypothesis

The issue was treated primarily as a runtime and environment-boundary problem, not as a Vue UI logic bug.

The main hypothesis was:

- the frontend runtime may be affected by the dev-container and Docker Compose boundary;
- Vite HMR and file watching may need Docker-friendly settings to stay stable inside the dev-container + Compose boundary;
- browser differences could still matter after the container/runtime layer was fixed.

## Problem-Solving Framework

The issue was approached in this order:

1. Confirm the boundary between the dev container and the Compose runtime.
2. Check whether source files actually reached the frontend container and whether the active runtime matched the environment where the bug appears.
3. Verify whether Vite dev server and HMR were configured for container execution.
4. Validate the frontend service from inside Compose, not only from the host.
5. Compare browser behavior between the working and failing paths.

This framework helped separate three layers:

- file synchronization;
- dev server/HMR configuration;
- browser-specific behavior.

## Problem-Solving Done

The following changes and checks were performed:

1. The frontend Vite configuration was updated in [frontend/vite.config.ts](../frontend/vite.config.ts) to make the dev server container-friendly.
2. The dev server was configured with explicit host and port settings.
3. Polling-based file watching was enabled so Docker-based sync behaved more predictably.
4. HMR client settings were made explicit for access through `localhost:5173`.
5. The frontend service was rebuilt through Docker Compose.
6. The frontend HTTP endpoint was validated from inside the container and returned `200`.
7. The browser page was validated through Compose runtime and rendered normally in Chrome.

## Validation Results

| Check | Result |
|---|---|
| `npm run build-only` in `frontend/` | Passed |
| `docker compose up -d --build frontend` | Passed |
| `docker compose logs frontend` | No startup error observed |
| HTTP probe to `http://127.0.0.1:5173` from inside the container | Returned `200` |
| Chrome on `http://localhost:5173` | Normal |
| Firefox on `http://localhost:5173` | Abnormal, unresolved |

## Browser Anomaly

| Browser | Behavior | Status |
|---|---|---|
| Google Chrome | Frontend page works normally after the runtime fix | Resolved |
| Mozilla Firefox | Frontend behavior remains abnormal compared with Chrome | Unresolved |

## Suspected Cause of the Firefox Anomaly

**Unresolved hypothesis:** Firefox may still be less tolerant of the current Vite HMR / WebSocket / file-watch interaction in this containerized setup.

This is only a suspicion, not a confirmed root cause.

Possible directions to investigate later:

- Firefox WebSocket handshake behavior;
- HMR client connection timing;
- browser cache or extension interference;
- Firefox-specific network or security handling.

## Why This Matters

This documentation is useful because the failure was not a single-layer bug.

The issue spanned:

- container runtime behavior;
- file synchronization;
- dev server configuration;
- browser-specific behavior.

That means the correct troubleshooting path was to stabilize the runtime first, then separate Chrome and Firefox behavior.

## Current Conclusion

The frontend runtime problem in the dev container was reduced by fixing the Docker/Vite execution path.

However, the Firefox anomaly is still not fully explained and should remain marked as **unresolved** until browser-level debugging confirms the cause.
