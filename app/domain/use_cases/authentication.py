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

    def authenticate_user(self, email: str, password: str) -> str:
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.password_service.verify_password(password, user.password_hash):
            return None

        access_token_expiration = 30  # in minutes
        access_token = self.token_service.generate_access_token(
            data={"email": user.email, "user_id": user.id}
            , expires_delta=access_token_expiration
        )
        return access_token
