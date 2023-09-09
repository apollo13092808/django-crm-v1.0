from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ========== SQLite ==========
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # ========== PostgreSQL ==========
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db_name',
#         'USER': 'username',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# ========== MySQL ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}

# # ========== MSSQL SERVER ==========
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'dbname',
#         'USER': 'username',
#         'PASSWORD': 'password',
#         'HOST': 'server_name',
#         'PORT': '',

#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

# # Set this to False if you want to turn off pyodbc's connection pooling
# DATABASE_CONNECTION_POOLING = False
