# Docker Daemon Not Ready For Dev Container

## Problem

`Dev Containers: Reopen in Container` can fail when Docker Desktop is already open, but the Docker daemon is not yet reachable from the dev container.

## What We Observed

- `Cannot connect to the Docker daemon at unix:///var/run/docker.sock`
- `docker compose ps` fails inside the dev container
- Reopen in Container stops during startup
- Docker Desktop is visible and the app containers may already be running, but the dev container still cannot talk to the daemon

## Root Cause

This workspace uses Docker-outside-of-Docker (DOOD).

That means the dev container does not run its own Docker daemon. It talks to the host Docker daemon through `/var/run/docker.sock`.

When Docker Desktop is still initializing, or the WSL integration is not ready yet, the socket may exist but the daemon is not yet reachable. The result is an immediate connection failure from the dev container.

## Fix

1. Open Docker Desktop on the host.
2. Wait until Docker Desktop is fully ready.
3. If the project is opened from WSL, enable WSL integration for that distro in Docker Desktop.
4. Reopen the repository in Dev Container.
5. After the container opens, verify the daemon is reachable:

First time using the dev container:
 - Run **Dev Containers: Rebuild and Reopen in Container**

```bash
docker compose ps
```

## Why This Is the Correct Fix

- No source code change is required.
- The failure is environmental, not application logic.
- Starting Docker Desktop restores the external daemon dependency that the dev container uses.
- WSL integration is required when the workspace is opened from WSL.

## Notes

- If Docker Desktop is already open but the daemon is still unavailable, wait a few seconds and retry.
- Docker Desktop can appear ready in the UI before the daemon socket is fully reachable.
- If the issue repeats after reopening, restart Docker Desktop before trying again.
- Only change code or configuration if the workspace itself is broken, not when the host daemon is simply not ready yet.
