import os
from .settings import BASE_DIR

# Set the secret key securely from the environment
SECRET_KEY = os.environ['SECRET']

# Set ALLOWED_HOSTS from the environment variable, default to Azure's hostname if not present
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'pizzamanager-ecbha3bfhqf6d3g7.northeurope-01.azurewebsites.net')]

# CSRF_TRUSTED_ORIGINS is required for Azure deployment to prevent CSRF errors
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('WEBSITE_HOSTNAME', 'pizzamanager-ecbha3bfhqf6d3g7.northeurope-01.azurewebsites.net')]

# Set Debug to True for now (it should be False in production, update accordingly)
DEBUG = True

# WhiteNoise configuration to serve static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Azure PostgreSQL connection string
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params.get('dbname'),
        'USER': conn_str_params.get('user'),
        'PASSWORD': conn_str_params.get('password'),
        'HOST': conn_str_params.get('host'),
        'PORT': conn_str_params.get('port', '5432'),
    }
}
