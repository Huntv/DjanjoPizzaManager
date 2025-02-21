import os
from django.core.wsgi import get_wsgi_application

settings_module = 'DjanjoPizzaManager.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'DjangoPizzaManager.settings'

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
        'DjanjoPizzaManager.settings')

application = get_wsgi_application()
