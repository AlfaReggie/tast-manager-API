from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskRead


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    owner = db.get(User, task_in.owner_id)
    if owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")

    task = Task(
        title=task_in.title,
        description=task_in.description,
        status=task_in.status,
        owner_id=task_in.owner_id,
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/", response_model=list[TaskRead])
def list_tasks(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    stmt = select(Task).order_by(Task.id).limit(limit).offset(offset)
    tasks = db.scalars(stmt).all()
    return tasks


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task