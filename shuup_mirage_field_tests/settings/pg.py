from .base import *  # noqa: F401,F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mirage",
        "USER": "yindongliang",
        "PASSWORD": "yindongliang",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
