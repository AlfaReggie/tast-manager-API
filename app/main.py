from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import Base, engine
from app.models import Task, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}