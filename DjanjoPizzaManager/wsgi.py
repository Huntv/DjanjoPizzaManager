import os
from django.core.wsgi import get_wsgi_application


# Set the default settings module if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DjanjoPizzaManager.settings)

# Get the WSGI application for Django
application = get_wsgi_application()
