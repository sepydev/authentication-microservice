class IntegrityError(Exception):
    ...


class UserOrPasswordIsWrong(ValueError):
    def __int__(self):
        super().__init__('Incorrect email or password.')
