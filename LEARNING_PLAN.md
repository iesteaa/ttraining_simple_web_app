# End-to-End Web Development Learning Plan

This document defines the learning sequence for the project. Each stage introduces a limited set of concepts and applies them directly to the task-management application.

## Learning Method

Every stage follows this process:

```text
Concept
   ↓
Small implementation
   ↓
Manual test
   ↓
Failure test
   ↓
Explanation in your own words
   ↓
Progress update
   ↓
Git commit
```

Do not move to the next stage only because the code runs. Move forward after you can also explain what the code does and why it is needed.

---

## Phase 0 — Development Environment

**Status:** Complete

### Concepts

- Project root and folder separation
- Python virtual environment
- Node.js dependencies
- Git repository
- `.gitignore`
- Development servers

### Implementation

- Create `backend/` and `frontend/`
- Create Python `.venv`
- Install FastAPI dependencies
- Create Vue 3 project with TypeScript
- Run both development servers

### Checkpoint

- [x] Backend environment works
- [x] Frontend environment works
- [x] Git repository is initialized
- [x] Local dependencies are ignored by Git

---

## Phase 1 — FastAPI and HTTP Fundamentals

**Status:** Complete

### Concepts

- FastAPI application object
- Server, request, and response
- Route and endpoint
- HTTP method and URL path
- JSON response
- Swagger UI and OpenAPI

### Implementation

```text
GET /
GET /health
```

### Checkpoint

- [x] FastAPI application starts
- [x] `/docs` displays the API
- [x] Root endpoint returns a response
- [x] Health endpoint returns a response
- [x] Learner can explain method + path = endpoint

---

## Phase 2 — Request Validation and Create/Read Operations

**Status:** Complete

### Concepts

- Request body
- Pydantic model
- Input schema and response schema
- Automatic validation
- `201 Created`
- `422 Unprocessable Entity`
- In-memory storage

### Implementation

```text
POST /tasks
GET  /tasks
GET  /tasks/{task_id}
```

### Checkpoint

- [x] `TaskCreate` schema exists
- [x] `Task` response schema exists
- [x] Valid task creation returns `201`
- [x] Invalid input returns `422`
- [x] All tasks can be retrieved
- [x] One task can be retrieved by ID
- [x] Missing task returns `404`

---

## Phase 3 — Update and Delete Operations

**Status:** Complete

### Concepts

- Partial update
- `PATCH` versus full replacement
- Optional fields
- `model_dump(exclude_unset=True)`
- `model_copy(update=...)`
- List index versus resource ID
- `204 No Content`

### Implementation

```text
PATCH  /tasks/{task_id}
DELETE /tasks/{task_id}
```

### Checkpoint

- [x] `TaskUpdate` schema exists
- [x] Title can be updated independently
- [x] Completed state can be updated independently
- [x] Unsent fields are preserved
- [x] Empty update is rejected
- [x] Task can be deleted by ID
- [x] Successful deletion returns `204`
- [x] Deleted task can no longer be retrieved

---

## Phase 4 — Modular Backend Routing

**Status:** Complete

### Concepts

- Separation of responsibilities
- Python package and `__init__.py`
- FastAPI `APIRouter`
- Router prefix and tags
- `app.include_router(...)`
- Refactoring without changing behavior

### Implementation

```text
main.py
app/schemas.py
app/routers/tasks.py
```

### Checkpoint

- [x] Schemas are separated from routes
- [x] Task endpoints use `APIRouter`
- [x] Router is included in the main application
- [x] CRUD behavior remains unchanged
- [x] Endpoints use a consistent `/tasks` resource path

---

## Phase 5 — SQLite and SQLAlchemy Persistence

**Status:** Next

### Concepts

- Database, table, row, and column
- Primary key
- SQLite
- SQLAlchemy ORM
- Database engine
- Session and transaction
- `commit`, `refresh`, and query
- ORM model versus Pydantic schema
- FastAPI dependency injection with `Depends`

### Planned Structure

```text
backend/app/
├── database.py
├── models.py
├── schemas.py
└── routers/
    └── tasks.py
```

### Implementation Goals

- Install SQLAlchemy
- Configure SQLite connection
- Create `Task` ORM model
- Create task table
- Create database session dependency
- Replace the in-memory list with database queries
- Preserve the existing API contract

### Checkpoint

- [ ] SQLAlchemy is installed
- [ ] SQLite database file is created
- [ ] `database.py` creates the engine and session factory
- [ ] `models.py` defines the Task table
- [ ] `POST /tasks` inserts a database row
- [ ] `GET /tasks` queries the database
- [ ] `GET /tasks/{task_id}` queries by primary key
- [ ] `PATCH /tasks/{task_id}` updates a database row
- [ ] `DELETE /tasks/{task_id}` deletes a database row
- [ ] Data remains after backend restart
- [ ] Learner can explain schema versus ORM model

---

## Phase 6 — Automated Backend Tests

**Status:** Pending

### Concepts

- Automated testing
- Test isolation
- Arrange, Act, Assert
- FastAPI `TestClient`
- Pytest fixtures
- Temporary test database
- Regression testing

### Implementation Goals

Test at least:

```text
POST success and validation failure
GET all
GET one
GET missing task
PATCH success and invalid input
DELETE success and missing task
```

### Checkpoint

- [ ] Pytest is installed
- [ ] TestClient can call the FastAPI application
- [ ] Tests use isolated database data
- [ ] Success paths are tested
- [ ] Error paths are tested
- [ ] All tests pass from one command

---

## Phase 7 — Configuration and CORS

**Status:** Pending

### Concepts

- Environment variables
- Application settings
- `.env` and `.env.example`
- Browser origin
- CORS policy
- Allowed frontend origin

### Implementation Goals

- Create backend settings
- Add `.env.example`
- Allow the Vue development origin
- Verify that the browser can call FastAPI

### Checkpoint

- [ ] Backend configuration is not hardcoded unnecessarily
- [ ] `.env` is ignored by Git
- [ ] `.env.example` documents required variables
- [ ] Vue origin is allowed by CORS
- [ ] Browser request succeeds without a CORS error

---

## Phase 8 — First Frontend-Backend Wiring

**Status:** Pending

### Concepts

- `fetch` or API client function
- Asynchronous request
- Loading, success, and error state
- Vue reactive state
- API response typing with TypeScript

### Implementation Goals

```text
Vue → GET /tasks
Vue → POST /tasks
Vue → PATCH /tasks/{task_id}
Vue → DELETE /tasks/{task_id}
```

### Checkpoint

- [ ] Vue displays tasks from the backend
- [ ] Create form sends a POST request
- [ ] Task completion sends a PATCH request
- [ ] Delete button sends a DELETE request
- [ ] UI updates after successful requests
- [ ] Loading state is visible
- [ ] Error feedback is visible

---

## Phase 9 — Better Backend Structure

**Status:** Pending

This phase starts after the first complete frontend-backend flow works.

### Concepts

- Router layer
- Service layer
- Repository layer
- Dependency injection
- Business logic separation
- Reusable database operations
- Logging

### Checkpoint

- [ ] Route functions are not responsible for every detail
- [ ] Business rules can be tested separately
- [ ] Database operations are reusable
- [ ] Errors are handled consistently

---

## Phase 10 — Database Migration and Production-Oriented Features

**Status:** Pending

### Concepts

- Alembic migration
- Database constraints
- Pagination and filtering
- Authentication and authorization
- Password hashing
- Security basics
- Docker
- Deployment configuration
- Integration testing

These topics are intentionally delayed until the basic end-to-end application is understood.

---

## Definition of a Completed Stage

A stage is complete when:

- [ ] The feature works
- [ ] Successful behavior was tested
- [ ] Failure behavior was tested
- [ ] The learner can explain the request flow
- [ ] The progress file was updated
- [ ] A Git commit was created

