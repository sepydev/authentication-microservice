from abc import ABC, abstractmethod


class IPasswordService(ABC):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        # Implementation details for hashing a password using a secure algorithm
        pass

    @abstractmethod
    def verify_password(self, password: str, password_hash: str) -> bool:
        # Implementation details for verifying a password against a stored password hash
        pass
