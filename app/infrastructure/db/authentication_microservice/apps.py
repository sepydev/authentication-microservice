from django.apps import AppConfig
from ..settings.settings import BASE_DJANGO_APP_PATH


class AuthenticationMicroserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = BASE_DJANGO_APP_PATH + 'authentication_microservice'
