"""
Development SETTINGS CONFIGURATIONS
"""

from djcommerce.settings.base import *

# Debug MODE
DEBUG = True

# Local .sqlite3 database during development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}