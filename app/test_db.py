from app.db.database import SessionLocal
from app.models.user import User


def main():
    db = SessionLocal()

    try:
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="not_real_hash_yet",
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"User created: id={user.id}, email={user.email}, username={user.username}")
    finally:
        db.close()


if __name__ == "__main__":
    main()