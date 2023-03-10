import environ

env = environ.Env()
environ.Env.read_env('.env')

ACCESS_TOKEN_EXPIRE_MINUTES = int(env('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = env('SECRET_KEY')
ALGORITHM = env('ALGORITHM')
DEBUG = env('DEBUG')
BROKER = env('BROKER')
