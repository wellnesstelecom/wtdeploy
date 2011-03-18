# -*- coding: utf-8 -*-

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#sorl-thumbnail
THUMBNAIL_DEBUG = True

#django-contact-form
DEFAULT_FROM_EMAIL = 'contactform@foo'

MANAGERS = (
    ('fooper','fooper@foo'),
)

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '%(database_name)s'             # Or path to database file if using sqlite3.
DATABASE_USER = '%(database_user)s'             # Not used with sqlite3.
DATABASE_PASSWORD = '%(database_pass)s'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

try:
   from mobile_local_settings import *
except ImportError:
   pass
