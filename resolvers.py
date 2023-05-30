import strawberry
from typing import Optional, List
from service import (
    get_user_by_id,
    get_all_users,
    create_new_user,
    update_existing_user,
    delete_existing_user,
)
from database import get_db
from schema import CreateUserInput, UpdateUserInput, UserType


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, input: CreateUserInput) -> UserType:
        db = next(get_db())
        new_user = create_new_user(db, input.name, input.email, input.age)
        return UserType(
            id=str(new_user.id),
            name=new_user.name,
            email=new_user.email,
            age=new_user.age,
        )

    @strawberry.mutation
    def update_user(
        self,
        user_id: strawberry.ID,
        input: UpdateUserInput,
    ) -> Optional[UserType]:
        db = next(get_db())
        user = get_user_by_id(db, int(user_id))
        if user:
            updated_user = update_existing_user(
                db, user, input.name, input.email, input.age
            )
            return UserType(
                id=str(updated_user.id),
                name=updated_user.name,
                email=updated_user.email,
                age=updated_user.age,
            )
        return None

    @strawberry.mutation
    def delete_user(
        self,
        user_id: strawberry.ID,
    ) -> bool:
        db = next(get_db())
        user = get_user_by_id(db, int(user_id))
        if user:
            return delete_existing_user(db, user)
        return False


@strawberry.type
class Query:
    @strawberry.field
    def get_user(
        self,
        user_id: strawberry.ID,
    ) -> Optional[UserType]:
        db = next(get_db())
        user = get_user_by_id(db, int(user_id))
        if user:
            return UserType(
                id=str(user.id), name=user.name, email=user.email, age=user.age
            )
        return None

    @strawberry.field
    def get_users(self) -> List[UserType]:
        db = next(get_db())
        users = get_all_users(db)
        return [
            UserType(id=str(user.id), name=user.name, email=user.email, age=user.age)
            for user in users
        ]


schema = strawberry.Schema(query=Query, mutation=Mutation)
