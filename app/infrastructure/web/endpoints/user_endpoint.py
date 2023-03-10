from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from lagom.integrations.fast_api import FastApiIntegration
from pydantic import ValidationError

from config_di import container
from ..controller import authenticate
from ..schemas.token_schema import Token
from ..schemas.user_schema import User, UserCreate
from ....domain.entities.exception import IntegrityError, UserOrPasswordIsWrong
from ....domain.use_cases.authentication import AuthenticationUseCase
from ....domain.use_cases.user import UserUseCase

api = FastAPI()
deps = FastApiIntegration(container)




@api.post("/users", response_model=User)
async def create_user(user_create: UserCreate, user_use_case=deps.depends(UserUseCase)):
    try:
        user = user_use_case.create_user(
            user_create.email,
            user_create.password,
            user_create.first_name,
            user_create.last_name
        )
        return user
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email address already exists."
        )
    except ValidationError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@api.post("/login", response_model=Token)
async def login(
        user_login: OAuth2PasswordRequestForm = Depends(),
        auth_use_case=deps.depends(AuthenticationUseCase)
):
    try:
        token = auth_use_case.get_token(user_login.username, user_login.password)
        return token
    except UserOrPasswordIsWrong as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@api.get("/users/me", response_model=User)
async def get_user_detail(user=Depends(authenticate)):
    return user
