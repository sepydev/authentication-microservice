import os
import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.infrastructure.db.settings.settings')
    os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")
    django.setup()


main()
