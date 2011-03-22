# -*- coding: utf-8 -*-

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Your Name', 'your_email@domain.com'),
)


MANAGERS = ADMINS

CACHE_BACKEND = 'dummy://'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%(database_name)s',                      # Or path to database file if using sqlite3.
        'USER': '%(database_user)s',                      # Not used with sqlite3.
        'PASSWORD': '%(database_pass)s',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


try:
   from mobile_local_settings import *
except ImportError:
   pass
