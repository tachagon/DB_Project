"""
Django settings for DB_Project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/site_media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#i&mumh&w2t%%-8w_9=du*)fg^do1r&1iy%gry9*#=^4ihu0-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'login',
    'group1',
    'group2',
    'group3',
    'group4',
    'group5',
    'group6',
    'group7',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DB_Project.urls'

WSGI_APPLICATION = 'DB_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), "")
LOGIN_URL = '/login/login/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'documentece01@gmail.com'
EMAIL_HOST_PASSWORD = 'adminece'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#---------------------------------------------- Create Log file --------------------------------------------------------
# define CONSTANCE variable
LOGFILE_NAME = os.path.join(BASE_DIR, 'logs/DB_Project.log')
LOGFILE_SIZE = 1024 * 1024 * 15 # 15 MB
LOGFILE_COUNT = 10              # 10 historical versions

LOGGING = {
    'version': 1,
    'disable_exiting_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
    },
    'handlers': {
        'logfile':{
            'level': 'DEBUG',
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_NAME,
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
#-----------------------------------------------------------------------------------------------------------------------



























