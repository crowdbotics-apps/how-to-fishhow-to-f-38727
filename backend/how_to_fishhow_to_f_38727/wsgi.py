"""
WSGI config for how_to_fishhow_to_f_38727 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'how_to_fishhow_to_f_38727.settings')

application = get_wsgi_application()
