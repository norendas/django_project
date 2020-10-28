"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/noren/Desktop/DjangoFolder/django_project/venv/lib/python3.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/noren/Desktop/DjangoFolder/django_project/django_project')
sys.path.append('/home/noren/Desktop/DjangoFolder/django_project/django_project/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()
