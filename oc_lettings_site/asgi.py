"""
ASGI config for oc_lettings_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# In production set :
# DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings.local')

application = get_asgi_application()
