import os

ENV = os.getenv("DJANGO_ENV", "local")

match ENV:
    case "dev":
        from .dev import *
    case "test":
        from .test import *
    case _:
        from api.core.settings.base import *
