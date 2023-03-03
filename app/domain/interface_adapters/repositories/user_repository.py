from typing import Optional
from app.domain.entities.user import User


class UserRepository:
    def get_user_by_email(self, email: str) -> Optional[User]:
        # Implementation details for retrieving a user from the database by email
        pass

    def create_user(self, user: User) -> User:
        # Implementation details for creating a new user in the database
        pass
