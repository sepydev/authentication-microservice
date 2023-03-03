from typing import Optional
from app.domain.entities.user import User
from app.domain.interface_adapters.repositories.user_repository import UserRepository
from app.domain.interface_adapters.services.token_service import TokenService
from app.domain.interface_adapters.services.password_service import PasswordService


class AuthenticationUseCase:
    def __init__(
            self,
            user_repository: UserRepository,
            token_service: TokenService,
            password_service: PasswordService,
    ):
        self.user_repository = user_repository
        self.token_service = token_service
        self.password_service = password_service

    def authenticate_user(self, email: str, password: str) -> Optional[str]:
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.password_service.verify_password(password, user.password_hash):
            return None
        access_token = self.token_service.generate_access_token(user.id)
        return access_token

    def create_user(self, email: str, password: str, full_name: Optional[str]) -> User:
        password_hash = self.password_service.hash_password(password)
        user = User(email=email, password_hash=password_hash, full_name=full_name)
        self.user_repository.create_user(user)
        return user
