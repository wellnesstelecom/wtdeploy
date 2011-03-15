#!/usr/bin/python 

import os, sys

def add_python_path():
  import sys, os
  import site
  root = os.path.dirname(__file__)
  paths = (
    os.path.join(root, "app"),
    os.path.join(root, "env/lib/python2.6/site-packages/"),
  )
  for path in paths:
      if not path in sys.path:
          sys.path.insert(0, path)

  # add virtualenv
  site.addsitedir(os.path.join(root, "env/lib/python2.6/site-packages/"))


add_python_path()
# Get rid of 'sys.stdout access restricted by mod_wsgi' error
sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

