from . import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': os.environ.get('DB_NAME') , # le nom de notre base de données créée précédemment
        'USER': os.environ.get('DB_USER'), # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '5432',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Purbeurre Team <noreply@purbeurre.com>' 
