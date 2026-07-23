# End-to-End Web Learning Project

A simple task-management web application built as a **learning-by-practice repository** for understanding how a frontend, backend, API, database, testing, and deployment fit together.

This repository is intentionally developed step by step. Each stage introduces one main concept, applies it in code, tests it, and records the result before moving forward.

## Learning Goal

By completing this project, learners should be able to understand and build this flow:

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
SQLite database
      ↓
JSON response
      ↓
Vue state and UI update
```

## Current Status

```text
Environment setup             ✅ Complete
Vue + TypeScript setup        ✅ Complete
FastAPI server                ✅ Complete
Task CRUD API                 ✅ Complete
Validation and HTTP errors    ✅ Complete
APIRouter refactor            ✅ Complete
SQLite + SQLAlchemy           ⏭️ Next stage
Automated backend tests       ⏳ Pending
CORS configuration            ⏳ Pending
Frontend-backend wiring       ⏳ Pending
```

The backend currently stores task data in memory. Data disappears when the backend server restarts. The next stage replaces this temporary storage with SQLite and SQLAlchemy.

## Technology Stack

| Area | Technology |
|---|---|
| Frontend | Vue 3, Vite, TypeScript |
| Backend | Python, FastAPI |
| Validation | Pydantic |
| Routing | FastAPI `APIRouter` |
| Database | SQLite and SQLAlchemy — planned |
| Backend testing | Pytest and FastAPI TestClient — planned |
| Version control | Git |
| Development environment | Visual Studio Code, WSL Ubuntu / Bash |

## Current Project Structure

```text
simple-web-app/
├── backend/
│   ├── .venv/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   └── routers/
│   │       ├── __init__.py
│   │       └── tasks.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── .gitignore
├── README.md
├── LEARNING_PLAN.md
└── PROGRESS.md
```

### Backend Responsibilities

```text
backend/main.py
→ Creates and configures the FastAPI application
→ Provides general endpoints such as / and /health
→ Includes feature routers

backend/app/schemas.py
→ Defines request and response schemas
→ Contains TaskCreate, TaskUpdate, and Task

backend/app/routers/tasks.py
→ Contains task CRUD endpoints
→ Handles task-related validation and HTTP errors
→ Currently uses temporary in-memory storage
```

## Implemented API

| Operation | Method | Endpoint | Expected result |
|---|---|---|---|
| Create task | `POST` | `/tasks` | `201 Created` |
| Read all tasks | `GET` | `/tasks` | `200 OK` |
| Read one task | `GET` | `/tasks/{task_id}` | `200 OK` or `404` |
| Update task | `PATCH` | `/tasks/{task_id}` | `200 OK` or `404` |
| Delete task | `DELETE` | `/tasks/{task_id}` | `204 No Content` or `404` |
| Health check | `GET` | `/health` | `200 OK` |

## Run the Backend

From the project root:

```bash
cd backend
source .venv/bin/activate
python -m pip install -r requirements.txt
fastapi dev --entrypoint main:app
```

Backend addresses:

```text
API:          http://127.0.0.1:8000
Swagger UI:   http://127.0.0.1:8000/docs
OpenAPI JSON: http://127.0.0.1:8000/openapi.json
```

## Run the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend normally runs at:

```text
http://localhost:5173
```

The frontend environment is ready, but the task interface and API connection have not yet been implemented.

## How to Use This Repository for Learning

Follow the repository in stage order rather than copying the final code immediately.

For each stage:

1. Read the concepts and target behavior in [`LEARNING_PLAN.md`](./LEARNING_PLAN.md).
2. Implement one small change.
3. Run the application.
4. Test both successful and failed cases.
5. Explain the request flow in your own words.
6. Update [`PROGRESS.md`](./PROGRESS.md).
7. Create a Git commit before starting the next stage.

Recommended learning cycle:

```text
Understand
    ↓
Implement
    ↓
Run
    ↓
Test
    ↓
Debug
    ↓
Explain
    ↓
Commit
```

## Learning Documents

- [`LEARNING_PLAN.md`](./LEARNING_PLAN.md): ordered learning roadmap, concepts, implementation goals, and stage checkpoints.
- [`PROGRESS.md`](./PROGRESS.md): current project status, completed checkpoints, next tasks, and a reusable work-session log.

## Git Checkpoint Example

After completing a learning stage:

```bash
git status
git add .
git commit -m "Complete task router refactor"
```

Use small commits that describe one completed learning objective.

## Next Stage

The next stage is **SQLite and SQLAlchemy persistence**.

The goal is to replace:

```python
tasks: list[Task] = []
```

with persistent database storage so task data remains available after the backend restarts.

Planned new backend files:

```text
backend/app/database.py
backend/app/models.py
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

