from datetime import datetime, timedelta
from typing import Dict, Any

import jwt
from passlib.context import CryptContext

from app.domain.interfaces.services.token_service import ITokenService


class TokenService(ITokenService):
    def __init__(self, secret_key: str, algorithm: str, access_token_expiration: int):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expiration = access_token_expiration
        self.hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def generate_access_token(self, data: Dict[str, Any], expires_delta: int) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def verify_access_token(self, token: str) -> Dict[str, Any]:
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.PyJWTError:
            return {}
        return decoded_token
