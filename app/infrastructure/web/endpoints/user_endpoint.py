from fastapi import FastAPI, HTTPException, status
from passlib.context import CryptContext

from ..schemas.token_schema import Token, TokenData
from ..schemas.user_schema import User, UserCreate, UserLogin
from ...db.repositories.user_repository import UserRepository
from ....domain.use_cases.authentication import AuthenticationUseCase
from ....services.password_service import PasswordService
from ....services.token_service import TokenService

app = FastAPI()
user_repository = UserRepository()
password_service = PasswordService()
token_service = TokenService()
auth_use_case = AuthenticationUseCase(user_repository)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/users", response_model=User)
async def create_user(user_create: UserCreate):
    user = auth_use_case.create_user(user_create.email, user_create.password, user_create.first_name,
                                     user_create.last_name)
    return user


@app.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    user = auth_use_case.authenticate_user(user_login.email, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
            , detail="Incorrect email or password"
        )
    access_token = token_service.generate_access_token(
        data={"email": user.email, "user_id": user.id},
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=User)
async def read_users_me(token_data: TokenData):
    user = user_repository.get_user_by_id(token_data.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
