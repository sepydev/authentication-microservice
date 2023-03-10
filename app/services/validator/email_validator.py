import re


def validate(value):
    email = re.search(r'[\w.]+\@[\w.]+', value)
    if not email:
        raise ValueError('The email address is invalid.')
    return value
