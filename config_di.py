from lagom import Container, Singleton
from app.domain.interfaces.repositories.user_repository import IUserRepository
from app.domain.interfaces.services.password_service import IPasswordService
from app.domain.interfaces.services.token_service import ITokenService
from app.domain.use_cases.authentication import AuthenticationUseCase
from app.domain.use_cases.user import UserUseCase
# configure django this line has to be before importing Repositories
from app.infrastructure.db import configure  # noqa
from app.infrastructure.db.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService
from app.services.token_service import TokenService

# configure Dependency injection
container = Container()

container[IUserRepository] = Singleton(UserRepository)
container[IPasswordService] = Singleton(PasswordService)
container[ITokenService] = Singleton(TokenService)
container[AuthenticationUseCase] = Singleton(AuthenticationUseCase)
container[UserUseCase] = Singleton(UserUseCase)
