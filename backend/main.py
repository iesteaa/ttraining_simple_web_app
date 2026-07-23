from fastapi import FastAPI

from app.routers.tasks import router as tasks_router

app = FastAPI(
    title = "Simple Web app API",
    version="1.0.0"
)

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

app.include_router(tasks_router)
