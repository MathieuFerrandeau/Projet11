from . import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

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
