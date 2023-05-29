from sqlalchemy.orm import Session
from typing import Optional, List
from models import User
from repository import get_user, get_users, create_user, update_user, delete_user


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return get_user(db, user_id)


def get_all_users(db: Session) -> List[User]:
    return get_users(db)


def create_new_user(db: Session, name: str, email: str, age: int) -> User:
    return create_user(db, name, email, age)


def update_existing_user(
    db: Session, user: User, name: str, email: str, age: int
) -> User:
    return update_user(db, user, name, email, age)


def delete_existing_user(db: Session, user: User) -> bool:
    return delete_user(db, user)
