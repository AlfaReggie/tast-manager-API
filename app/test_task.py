from app.db.database import SessionLocal
from app.models.task import Task
from app.models.user import User


def main():
    db = SessionLocal()

    try:
        user = db.query(User).filter(User.email == "test@example.com").first()

        if user is None:
            print("User not found")
            return

        task = Task(
            title="Learn SQLAlchemy basics",
            description="Create first task linked to user",
            status="new",
            owner_id=user.id,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        print(
            f"Task created: id={task.id}, title={task.title}, "
            f"owner_id={task.owner_id}, status={task.status}"
        )
    finally:
        db.close()


if __name__ == "__main__":
    main()