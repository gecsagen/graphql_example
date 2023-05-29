from sqlalchemy.orm import Session
from models import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, name: str, email: str, age: int):
    new_user = User(name=name, email=email, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: User, name: str, email: str, age: int):
    user.name = name
    user.email = email
    user.age = age
    db.commit()
    return user


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return True
