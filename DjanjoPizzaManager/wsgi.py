import os
from django.core.wsgi import get_wsgi_application

# Set the settings module based on the environment (production or development)
# Set the default settings module if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjanjoPizzaManager')

# Get the WSGI application for Django
application = get_wsgi_application()
