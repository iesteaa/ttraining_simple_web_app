from typing import Annotated

from app.config import settings
from app.database import get_db
from app.routers.tasks import router as tasks_router
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

app = FastAPI(title="Simple Web app API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=False,  # cookie setup
    allow_methods=[
        "GET",
        "POST",
        "PATCH",
        "DELETE",
    ],
    allow_headers=[
        "Content-Type",
    ],
)

# Database-Endpoint Health Check!
DatabaseSession = Annotated[Session, Depends(get_db)]


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Backend server is running", "/docs": "do swagger UI Test"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok desu"}


@app.get("/health/database")
def database_health(db: DatabaseSession) -> dict[str, str]:
    db.execute(text("SELECT 1"))

    return {"status": "healthy"}


app.include_router(tasks_router)
