import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "botfactory_backend.settings.dev"
)
application = get_wsgi_application()
