from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    password_hash: str
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = None
