# Dev Container (DOOD)

This workspace uses a development container for editing and tooling while Docker Compose remains the runtime for application services.

## Runtime boundaries

- Dev Container: editor, shell, git, Python/Node tooling, Docker CLI.
- Compose services: `backend`, `frontend`, `db`, `db_test` from the root `compose.yaml`.

Docker CLI and Docker Compose CLI are provided by the Dev Containers DOOD feature.

## Why Docker-outside-of-Docker

The Dev Container mounts host Docker socket (`/var/run/docker.sock`) so commands run from the container terminal can control the host Docker daemon:

- `docker compose up`
- `docker compose ps`
- `docker compose logs`
- `docker compose exec`

## Open and verify

1. Reopen the repository in Dev Container.
2. Run `docker compose ps`.
3. Run VS Code tasks `backend: checks` and `frontend: checks`.

## First-Time Setup for New Developers

1. Ensure Docker is running on the host machine.
2. Open the repository in VS Code and run `Dev Containers: Reopen in Container`.
3. Wait until container build and setup commands complete.
4. In the dev container terminal:

```bash
docker compose up -d --build
docker compose ps
```

5. Confirm runtime services are visible:
  - `backend` is running
  - `frontend` is running
  - `db` is healthy
  - `db_test` is healthy

## Verify DOOD Connectivity

Run these commands from inside the dev container terminal:

```bash
docker ps
docker compose ps
docker compose exec backend python -m pytest -q
docker compose exec frontend yarn lint
```

If all commands run successfully, the dev container can control host Docker daemon correctly via mounted socket.

## Verify SSH Agent Forwarding

After rebuilding or reopening the dev container, run these commands from inside the dev container terminal:

```bash
echo "$SSH_AUTH_SOCK"
ssh-add -l
ssh -T git@github.com
```

The `ssh-add -l` command should show the keys loaded in the host SSH agent. If it still says the agent cannot be reached, confirm that the host session has an active `ssh-agent` and that a key has been added on the host before reopening the container.

## Expected Runtime Boundary

- Dev container: editor, terminal, git, local tooling.
- Compose runtime: `backend`, `frontend`, `db`, `db_test`.
- Application services remain defined in root `compose.yaml`.

## Common issues

- Permission denied for Docker socket:
  - Check host socket group: `ls -l /var/run/docker.sock`
  - Rebuild the Dev Container after UID/GID changes.
- Compose services not running:
  - Start stack from Dev Container terminal with `docker compose up -d --build`.
- Missing local tooling commands:
  - Re-run `postCreateCommand` manually:
    - `python3 -m pip install --user -r backend/requirements-dev.txt`
    - `npm ci --prefix frontend`
- Host port conflicts (`5432`, `5433`, `8000`, `5173`):
  - Stop conflicting process or container, then rerun `docker compose up -d --build`.
- Outdated container setup after configuration changes:
  - Run `Dev Containers: Rebuild Container`.
