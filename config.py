import environ
from lagom import Container
from app.domain.interfaces.repositories.user_repository import IUserRepository
from app.infrastructure.db.repositories.user_repository import UserRepository

env = environ.Env()
environ.Env.read_env('.env')

ACCESS_TOKEN_EXPIRE_MINUTES = env('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY = env('SECRET_KEY')
ALGORITHM = env('ALGORITHM')
DEBUG = env('DEBUG')
BROKER = env('BROKER')

# configure Dependency injection
container = Container()
container[IUserRepository] = UserRepository()
