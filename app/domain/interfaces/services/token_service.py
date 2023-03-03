from abc import ABC, abstractmethod
from typing import Dict, Any


class ITokenService(ABC):
    @abstractmethod
    def generate_access_token(self, data: Dict[str, Any], expires_delta: int = None) -> str:
        pass

    @abstractmethod
    def verify_access_token(self, token: str) -> Dict[str, Any]:
        pass
