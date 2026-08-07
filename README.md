# End-to-End Web Learning Project

A small task-management web application used to learn and demonstrate how a frontend, backend, API, database, testing, and Docker Compose workflow fit together.

The repository is written as a learning log, but it is also intended to be readable during a supervisor review. The documentation therefore focuses on what exists now, how to run it, and what remains next.

## Overview

Current state:

- The backend is fully implemented with FastAPI, SQLAlchemy, PostgreSQL, and automated tests.
- The frontend exists as a Vue 3 + TypeScript scaffold, but it is not yet wired to the backend.
- Docker Compose is the main runtime for local development.

Target application flow:

```text
User interaction
      ↓
Vue frontend
      ↓ HTTP request
FastAPI backend
      ↓
Business logic and validation
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL database
      ↓
JSON response
      ↓
Vue state and UI update
```

The diagram above describes the intended end-to-end flow for the later integration stage. The immediate next step is to implement a dev container as the VS Code workspace so the project can be opened and developed inside a containerized environment.

## Quick Start

1. Copy the example environment files if you do not already have local ones:

```bash
cp .env.example .env
cp .env.test.example .env.test
```

2. Start the full application runtime with Docker Compose:

```bash
docker compose up --build
```

3. Keep VS Code running locally in WSL and use the workspace tasks for format, lint, typecheck, and tests. Those tasks execute through `docker compose exec`.

## Current Status

```text
Environment setup             ✅ Complete
FastAPI CRUD API              ✅ Complete
SQLAlchemy + PostgreSQL       ✅ Complete
Docker Compose runtime        ✅ Complete
Automated backend tests       ✅ Complete
CORS configuration            ✅ Complete
Frontend scaffold             ✅ Complete
Dev container workspace       ⏳ Pending
Frontend-backend wiring       ⏳ Pending
```

The backend persists task data through SQLAlchemy and PostgreSQL. The application runtime is containerized with Docker Compose, while VS Code stays local in WSL. The frontend scaffold is present, but it still needs the API client and task UI work after the dev container workspace stage is completed.

## Technology Stack

| Area | Technology |
|---|---|
| Frontend | Vue 3, Vite, TypeScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Runtime | Docker, Docker Compose |
| Testing | Pytest, FastAPI TestClient, Vitest |
| Tooling | Ruff, ESLint, Oxlint, Prettier |
| Development environment | Visual Studio Code, WSL Ubuntu / Bash |

## Version Requirements

These versions are pinned or documented so the setup stays reproducible across machines:

| Component | Version |
|---|---|
| Python | 3.12.10 |
| Node.js | 22.x |
| PostgreSQL | 17.10 |

Source of truth:

- Python version: [`.python-version`](./.python-version)
- Backend image: [`backend/Dockerfile`](./backend/Dockerfile)
- Frontend engine requirement: [`frontend/package.json`](./frontend/package.json)
- Database image: [`compose.yaml`](./compose.yaml)

## What Is Implemented

- FastAPI application with `/`, `/health`, and CRUD task endpoints.
- PostgreSQL-backed persistence with SQLAlchemy and Alembic.
- Automated backend tests with isolated database fixtures.
- Docker Compose services for backend, frontend, and database.
- VS Code tasks that run format, lint, typecheck, and tests inside containers.
- Local WSL editing with containerized application runtime.

## Development Tooling

The project uses separate quality-check commands for backend and frontend code. Some checks run automatically when you save files in VS Code, while others are exposed as VS Code tasks for verification before commit.

### Backend

- Format on save: VS Code formats Python files automatically with Ruff when you save them.
- Import sorting on save: VS Code also applies `source.organizeImports` for Python files, so import cleanup happens alongside formatting.
- Format check: `docker compose exec backend env RUFF_CACHE_DIR=/tmp/ruff-cache python -m ruff format --check .`
- Lint: `docker compose exec backend python -m ruff check .`
- Type check: `docker compose exec backend python -m mypy .`
- Tests: `docker compose exec backend python -m pytest -q`

How to use it:

1. Open a Python file in the backend.
2. Make your changes and save the file to let VS Code apply Ruff formatting and import sorting automatically.

Or use `Ctrl + Shift + P` -> `Tasks: Run Task`.
1. Run the `backend: format check` task in VS Code before committing to confirm the file still matches the formatter.
2. Run `backend: checks` when you want the full backend verification sequence.

### Frontend

- Format check: `docker compose exec frontend yarn format:check`
- Lint: `docker compose exec frontend yarn lint`
- Type check: `docker compose exec frontend yarn type-check`
- Unit tests: `docker compose exec frontend yarn test:unit`

The frontend package also exposes local equivalents through `frontend/package.json`:

- `yarn dev`
- `yarn build`
- `yarn lint`
- `yarn format:check`
- `yarn test:unit`

### Workspace tasks

- `backend: checks` runs backend format, lint, typecheck, and tests in sequence.
- `frontend: checks` runs frontend format, lint, and typecheck in sequence.

## Implemented API

| Operation | Method | Endpoint | Expected result |
|---|---|---|---|
| Create task | `POST` | `/tasks` | `201 Created` |
| Read all tasks | `GET` | `/tasks` | `200 OK` |
| Read one task | `GET` | `/tasks/{task_id}` | `200 OK` or `404` |
| Update task | `PATCH` | `/tasks/{task_id}` | `200 OK` or `404` |
| Delete task | `DELETE` | `/tasks/{task_id}` | `204 No Content` or `404` |
| Database health | `GET` | `/health/database` | `200 OK` or database error |
| Health check | `GET` | `/health` | `200 OK` |

## Run the Application with Docker Compose

This repository is set up so the application runtime runs in Docker Compose while VS Code stays local in WSL. Edit code in the workspace as usual, then start the services from the project root:

```bash
docker compose up --build
```

The backend and frontend use bind mounts, so file changes in WSL are reflected inside the containers.

The backend expects PostgreSQL connection values from the root `.env` file, and inside Compose it reaches the database through the service name `db`:

```text
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
POSTGRES_HOST
POSTGRES_PORT
CORS_ORIGINS
```

For test runs, the Compose test database service is named `db_test`.

Development workflow summary:

- Edit code in WSL and save normally.
- Use `docker compose up --build` for the application runtime.
- Use the VS Code tasks in [`.vscode/tasks.json`](./.vscode/tasks.json) for checks.
- Keep `.env` and `.env.test` aligned with the Compose service names.

Application addresses:

```text
API:          http://127.0.0.1:8000
Swagger UI:   http://127.0.0.1:8000/docs
OpenAPI JSON: http://127.0.0.1:8000/openapi.json
Frontend:     http://localhost:5173
```

Use the VS Code tasks in [`.vscode/tasks.json`](./.vscode/tasks.json) for backend and frontend checks; they execute through `docker compose exec`.

Reproducibility notes:

- `docker compose up --build` is the primary entry point for the app runtime.
- Backend and frontend dependencies are installed inside images, not on the host.
- Python and Node versions are pinned or documented so the runtime matches across machines.
- PostgreSQL runs as the Compose service `db`, and test runs use `db_test`.

## Documentation

- [`LEARNING_PLAN.md`](./LEARNING_PLAN.md): stage roadmap and learning checkpoints.
- [`PROGRESS.md`](./PROGRESS.md): current progress, completed checkpoints, and next tasks.

## Next Stage

The next stage is **Dev Container Workspace**.

The goal is to move the project into a proper VS Code dev container workspace so the editor, tools, and application environment can run from the same containerized setup.

Planned focus:

```text
Dev container workspace
VS Code opens inside container
Shared toolchain and environment
Project tasks run in the container workspace
```

After that workspace step is in place, the backend API is ready for frontend integration work, and the frontend still needs the API service, task list, task form, completion toggle, delete action, and loading or error states.

## Repository Principle

This repository prioritizes understanding over speed.

The objective is not only to make the application work, but also to understand:

- where data comes from;
- how a request reaches the backend;
- how input is validated;
- where business logic is executed;
- how data is stored;
- how the frontend receives and displays the response;
- how errors are identified and tested.

