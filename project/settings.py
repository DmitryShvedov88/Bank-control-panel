import os
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env("ENGINE"),
        'HOST': env("HOST"),
        'PORT': env("PORT"),
        'NAME': env("NAME"),
        'USER': env("USER"),
        'PASSWORD': env("PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': env("APP_DIRS"),
    },
]


USE_L10N = env("USE_L10N")

LANGUAGE_CODE = env("LANGUAGE_CODE")

TIME_ZONE = env("TIME_ZONE")

USE_TZ = env("USE_TZ")

DEFAULT_AUTO_FIELD = env("DEFAULT_AUTO_FIELD")
