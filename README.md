# End-to-End Web Learning Project

A small task-management web application used to learn and demonstrate how a frontend, backend, API, database, testing, and Docker Compose workflow fit together.

The repository is written as a learning log, but it is also intended to be readable during a supervisor review. The documentation therefore focuses on what exists now, how to run it, and what remains next.

## Overview

Current application flow:

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
CORS configuration            ⏳ Pending
Frontend-backend wiring       ⏳ Pending
```

The backend persists task data through SQLAlchemy and PostgreSQL. The application runtime is containerized with Docker Compose, while VS Code stays local in WSL.

## Technology Stack

| Area | Technology |
|---|---|
| Frontend | Vue 3, Vite, TypeScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Runtime | Docker, Docker Compose |
| Testing | Pytest, FastAPI TestClient, Vitest |
| Tooling | Black, Ruff, ESLint, Oxlint, Prettier |
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
```

For test runs, the Compose test database service is named `db_test`.

Development workflow summary:

- Edit code in WSL and save normally.
- Python files are formatted on save in VS Code, and imports are organized on save.
- Use `docker compose up --build` for the application runtime.
- Use the VS Code tasks in [`.vscode/tasks.json`](./.vscode/tasks.json) for lint, typecheck, and tests.
- Keep `.env` and `.env.test` aligned with the Compose service names.

Application addresses:

```text
API:          http://127.0.0.1:8000
Swagger UI:   http://127.0.0.1:8000/docs
OpenAPI JSON: http://127.0.0.1:8000/openapi.json
Frontend:     http://localhost:5173
```

Use the VS Code tasks in [`.vscode/tasks.json`](./.vscode/tasks.json) for backend and frontend checks; they execute through `docker compose exec`.
Python formatting and import organization happen automatically on save in VS Code.

Reproducibility notes:

- `docker compose up --build` is the primary entry point for the app runtime.
- Backend and frontend dependencies are installed inside images, not on the host.
- Python and Node versions are pinned or documented so the runtime matches across machines.
- PostgreSQL runs as the Compose service `db`, and test runs use `db_test`.

## Documentation

- [`LEARNING_PLAN.md`](./LEARNING_PLAN.md): stage roadmap and learning checkpoints.
- [`PROGRESS.md`](./PROGRESS.md): current progress, completed checkpoints, and next tasks.

## Next Stage

The next stage is **Configuration and CORS**.

The goal is to keep runtime configuration explicit and allow browser-based requests from the Vue frontend.

Planned focus:

```text
Backend settings
.env example files
Allowed frontend origin
CORS policy
```

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

