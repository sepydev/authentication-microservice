from datetime import datetime, timedelta
from typing import Dict, Any

import jwt

from app.domain.interfaces.services.token_service import ITokenService
from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


# from passlib.context import CryptContext


class TokenService(ITokenService):
    # def __init__(self):
    #     self.hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def generate_access_token(self, data: Dict[str, Any], expires_delta: int = None) -> str:
        if expires_delta is None:
            expires_delta = ACCESS_TOKEN_EXPIRE_MINUTES
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_access_token(self, token: str) -> Dict[str, Any]:
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.PyJWTError:
            return {}
        return decoded_token
