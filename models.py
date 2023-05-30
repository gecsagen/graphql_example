from sqlalchemy import Column, Integer, String
from database import Base
from typing import Any

class User(Base):
    __tablename__ = "users"

    id: Any = Column(Integer, primary_key=True, index=True)
    name: Any = Column(String)
    email: Any = Column(String, unique=True, index=True)
    age: Any = Column(Integer)
