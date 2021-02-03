"""
Production SETTINGS CONFIGURATIONS
"""

import os
from djcommerce.settings.base import *
import dj_database_url

# Debug MODE
DEBUG = False

# Local .sqlite3 database during development
DATABASES["default"] = dj_database_url.parse(
    os.getenv("DATABASE_URL"), conn_max_age=600
)