import os
from django.core.wsgi import get_wsgi_application

# Set the settings module based on the environment (production or development)
settings_module = 'DjanjoPizzaManager.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'DjanjoPizzaManager.settings'

# Set the default settings module if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# Get the WSGI application for Django
application = get_wsgi_application()