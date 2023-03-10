from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from lagom.integrations.fast_api import FastApiIntegration
from starlette import status

from app.domain.use_cases.authentication import AuthenticationUseCase
from config_di import container

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login', )
deps = FastApiIntegration(container)


def authenticate(token: str = Depends(oauth2_scheme), auth_use_case=deps.depends(AuthenticationUseCase)):
    try:
        user = auth_use_case.get_user_by_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
