"""
WSGI config for oc_lettings_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# In production set :
# DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings.local')

application = get_wsgi_application()
