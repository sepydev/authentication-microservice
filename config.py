from os import environ

env = environ.Env()

ACCESS_TOKEN_EXPIRE_MINUTES = env('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY = env('SECRET_KEY')
ALGORITHM = env('ALGORITHM')
DEBUG = env('DEBUG')
