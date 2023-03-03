from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    email: str
    password_hash: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: Optional[str] = None,
    last_name: Optional[str] = None
