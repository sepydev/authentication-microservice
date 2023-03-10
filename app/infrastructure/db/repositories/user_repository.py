from typing import Optional

import django.db
from django.contrib.auth import get_user_model

from app.domain.entities.exception import IntegrityError
from app.domain.entities.user import User
from app.domain.interfaces.repositories.user_repository import IUserRepository

UserModel = get_user_model()


class UserRepository(IUserRepository):
    def get_user_by_id(self, id: int) -> Optional[User]:
        try:
            django_user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return None
        user = User(
            id=django_user.id,
            email=django_user.email,
            first_name=django_user.first_name,
            last_name=django_user.last_name,
            password_hash=django_user.password,
        )
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            django_user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        user = User(
            id=django_user.id,
            email=django_user.email,
            first_name=django_user.first_name,
            last_name=django_user.last_name,
            password_hash=django_user.password,
        )
        return user

    def create_user(self, user: User) -> User:
        try:
            django_user = UserModel.objects.create_user(
                email=user.email,
                password_hash=user.password_hash,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            user.id = django_user.id
            return user
        except django.db.IntegrityError as error:
            raise IntegrityError(str(error))
