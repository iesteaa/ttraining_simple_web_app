# End-to-End Web Development Progress

**Last updated:** 2026-07-23  
**Current phase:** Backend Core v1 completed; preparing SQLite and SQLAlchemy integration

## Project Status

| Area | Status |
|---|---|
| Environment setup | ✅ Complete |
| Vue 3 + TypeScript environment | ✅ Complete |
| FastAPI server | ✅ Complete |
| Task CRUD API | ✅ Complete |
| Pydantic validation | ✅ Complete |
| HTTP status and error handling | ✅ Complete |
| APIRouter refactor | ✅ Complete |
| SQLite and SQLAlchemy | ⏭️ Next |
| Automated backend testing | ⏳ Pending |
| CORS | ⏳ Pending |
| Frontend task interface | ⏳ Pending |
| Frontend-backend wiring | ⏳ Pending |

## Completed Backend Checkpoints

### FastAPI Fundamentals

- [x] Created the FastAPI application object
- [x] Started the backend development server
- [x] Opened Swagger UI
- [x] Tested root and health endpoints
- [x] Understood routes and endpoints
- [x] Understood HTTP method + URL path

### Schemas and Validation

- [x] Created `TaskCreate`
- [x] Created `Task`
- [x] Created `TaskUpdate`
- [x] Used Pydantic `Field` validation
- [x] Observed automatic `422` responses
- [x] Understood input schema versus response schema

### Task CRUD

- [x] `POST /tasks`
- [x] `GET /tasks`
- [x] `GET /tasks/{task_id}`
- [x] `PATCH /tasks/{task_id}`
- [x] `DELETE /tasks/{task_id}`
- [x] Used `201 Created`
- [x] Used `204 No Content`
- [x] Used `400 Bad Request`
- [x] Used `404 Not Found`
- [x] Used `raise HTTPException(...)`

### Python and Partial Update Concepts

- [x] Used loops to find task data
- [x] Used `enumerate()`
- [x] Understood resource ID versus list index
- [x] Used `model_dump(exclude_unset=True)`
- [x] Used `model_copy(update=...)`
- [x] Used `tasks.pop(index)`
- [x] Understood why in-memory data disappears after restart

### Router Refactor

- [x] Created `app/` package
- [x] Created `app/routers/` package
- [x] Moved schemas to `app/schemas.py`
- [x] Moved task routes to `app/routers/tasks.py`
- [x] Added router prefix and tags
- [x] Included the router in `main.py`
- [x] Re-tested CRUD after refactoring
- [x] Standardized the task resource path as `/tasks`

## Current API Contract

```text
POST   /tasks
GET    /tasks
GET    /tasks/{task_id}
PATCH  /tasks/{task_id}
DELETE /tasks/{task_id}
GET    /health
```

## Immediate Next Checkpoint — Database Persistence

- [ ] Install SQLAlchemy
- [ ] Save the dependency to `requirements.txt`
- [ ] Create `app/database.py`
- [ ] Configure the SQLite database URL
- [ ] Create the SQLAlchemy engine
- [ ] Create a session factory
- [ ] Create the database-session dependency
- [ ] Create `app/models.py`
- [ ] Define the Task ORM model
- [ ] Create the task table
- [ ] Replace in-memory POST logic
- [ ] Replace in-memory GET logic
- [ ] Replace in-memory PATCH logic
- [ ] Replace in-memory DELETE logic
- [ ] Restart the backend
- [ ] Confirm that task data remains available
- [ ] Explain the difference between Pydantic schema and ORM model

## Later Checkpoints

### Automated Backend Testing

- [ ] Install and configure Pytest
- [ ] Use FastAPI TestClient
- [ ] Create an isolated test database
- [ ] Test successful CRUD behavior
- [ ] Test validation and missing-resource behavior

### CORS and Configuration

- [ ] Create backend `.env.example`
- [ ] Configure the Vue frontend origin
- [ ] Verify browser requests to the backend

### Frontend Wiring

- [ ] Create a typed frontend API service
- [ ] Display tasks from `GET /tasks`
- [ ] Create tasks with `POST /tasks`
- [ ] Update tasks with `PATCH /tasks/{task_id}`
- [ ] Delete tasks with `DELETE /tasks/{task_id}`
- [ ] Add loading feedback
- [ ] Add error feedback

## Work Session Log Template

Copy this section after each learning session.

```markdown
## Session: YYYY-MM-DD — Stage Name

### Goal

- What did I plan to learn or implement?

### Changes Made

- File changed:
- Endpoint or feature added:
- Configuration changed:

### Concepts Learned

- Concept 1:
- Concept 2:

### Tests Performed

- [ ] Successful case tested
- [ ] Invalid input tested
- [ ] Missing resource tested
- [ ] Behavior after restart tested, when relevant

### Problems and Debugging

- Error or unexpected behavior:
- Root cause:
- Fix:

### Result

- [ ] Completed
- [ ] Partially completed
- [ ] Needs review

### Next Action

- The next smallest task is:
```

## Update Rules

After every stage:

1. Change the **Last updated** date.
2. Update the **Current phase**.
3. Mark completed checklist items with `[x]`.
4. Add any new concepts learned.
5. Record important errors and fixes in the session log.
6. Keep unfinished tasks unchecked.
7. Commit the documentation together with the related code change.

Suggested commit example:

```bash
git add README.md LEARNING_PLAN.md PROGRESS.md backend
git commit -m "Document backend progress and database learning plan"
```

