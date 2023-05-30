import strawberry
from typing import Optional


@strawberry.type
class UserType:
    id: strawberry.ID
    name: str
    email: str
    age: int


@strawberry.input
class CreateUserInput:
    name: str
    email: str
    age: int


@strawberry.input
class UpdateUserInput:
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
