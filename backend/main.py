from fastapi import FastAPI, Depends

from app.routers.tasks import router as tasks_router
from app.database import get_db

from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI(
    title = "Simple Web app API",
    version="1.0.0"
)

# Database-Endpoint Health Check!
DatabaseSession = Annotated[Session, Depends(get_db)]

@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Backend server is running",
        "/docs": "do swagger UI Test"
    }

@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok desu"
    }

@app.get("/health/database")
def database_health(db: DatabaseSession) -> dict[str, str]:
    db.execute(text("SELECT 1"))

    return {"status": "healthy"}

app.include_router(tasks_router)
