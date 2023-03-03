from celery import Celery

from app.domain.use_cases.authentication import AuthenticationUseCase
from app.infrastructure.db.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService
from app.services.token_service import TokenService
from config import BROKER

app = Celery('tasks', broker=BROKER)


@app.task
def authenticate_user_task(username: str, password: str) -> str:
    user_repository = UserRepository()
    password_service = PasswordService()
    token_service = TokenService()

    use_case = AuthenticationUseCase(user_repository, password_service, token_service)
    access_token = use_case.authenticate_user(username, password)

    return access_token
