from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.tasks import router as tasks_router
from app.db.database import Base, engine
from app.models import Task, User  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Task Manager API",
    lifespan=lifespan,
)

app.include_router(tasks_router)


@app.get("/health")
def health():
    return {"status": "ok"}