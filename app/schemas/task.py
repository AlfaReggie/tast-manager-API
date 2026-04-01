from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "new"


class TaskCreate(TaskBase):
    owner_id: int


class TaskRead(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)