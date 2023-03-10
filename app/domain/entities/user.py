from typing import Optional

from pydantic import validator
from pydantic.dataclasses import dataclass

from ...services.validator import email_validator


@dataclass
class User:
    email: str
    password_hash: str
    id: Optional[int] = None
    is_active: bool = True
    is_superuser: bool = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @validator('email')
    def email_validator(cls, value):
        return email_validator.validate(value)
