from typing import Optional

from app.domain.entities.user import User
from app.domain.interfaces.repositories.user_repository import IUserRepository
from app.domain.interfaces.services.password_service import IPasswordService


class UserUseCase:
    def __init__(
            self,
            user_repository: IUserRepository,
            password_service: IPasswordService,
    ):
        self.user_repository = user_repository
        self.password_service = password_service

    def create_user(self, email: str, password: str, first_name: Optional[str], last_name: Optional[str]) -> User:
        password_hash = self.password_service.hash_password(password)
        user = User(email=email, password_hash=password_hash, first_name=first_name, last_name=last_name)
        self.user_repository.create_user(user)
        return user
