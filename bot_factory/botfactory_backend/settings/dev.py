from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "drf_spectacular",
    "drf_spectacular_sidecar",
]
