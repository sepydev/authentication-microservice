from typing import Optional

from app.domain.entities.exception import UserOrPasswordIsWrong
from app.domain.entities.user import User
from app.domain.interfaces.repositories.user_repository import IUserRepository
from app.domain.interfaces.services.password_service import IPasswordService
from app.domain.interfaces.services.token_service import ITokenService


class AuthenticationUseCase:
    def __init__(
            self,
            user_repository: IUserRepository,
            token_service: ITokenService,
            password_service: IPasswordService,
    ):
        self.user_repository = user_repository
        self.token_service = token_service
        self.password_service = password_service

    def _authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.password_service.verify_password(password, user.password_hash):
            raise UserOrPasswordIsWrong()
        return user

    def get_token(self, email: str, password: str) -> str:
        user = self._authenticate_user(email, password)
        access_token = self.token_service.generate_access_token(
            data={"email": user.email, "user_id": user.id},
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def get_user_by_token(self, token: str) -> Optional[User]:
        token_data = self.token_service.verify_access_token(token)
        user = self.user_repository.get_user_by_id(token_data['user_id'])
        return user
