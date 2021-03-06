"""
Django settings for camp200 project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import datetime
from pathlib import Path
from django.utils import timezone

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib.sites import requests

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vzb+d(zq#96@tek-jk4$(n5iz^3mo%7it$h)ux8oni(@#9$(04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'classroom',
    'dashboard',
    'catalogue',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'camp200.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'camp200.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'camp200',
        'USER': 'manager',
        'PASSWORD': 'manager123',
        'HOST': 'aurora.cjnwtxhdwz5m.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'templates')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates')]

# AWS

AWS_ACCESS_KEY = "AKIA4RTB2YTTOFUBDLMI"
AWS_SECRET_KEY = "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"
COURSES_IMAGES_BUCKET = "imgcourses"

# VIMEO
VIMEO_CLIENT_ID = "e46be3a6476f77ced4f52fe308aca606b0a103cc"
VIMEO_TOKEN = "4095fd2d54a0240ab70a231c3fdd2a43"

VIMEO_CLIENT_SECRETS = "N5w4mxnwZqvLV9V1CpCCKctx0z/HeCK0aJS3K2rrjPDV291GKdrv1Pmh2HmDnz8pH1HjqQdEcu2uEuSXnm52f+M5B2Wd0TM0Opq0i4rIJ2rGF+k2rF6mJpG8IbHaxtsH"
AUTH_USER_MODEL = 'catalogue.MyUser'

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_PASSWORD = 'fd8627ecaf36414fb7ff0f9a2d67fb3c-a09d6718-a034f401'
EMAIL_HOST_USER = 'postmaster@sandbox51dd1882705b4526b9d8c890e677f1b0.mailgun.org'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EXPIRATION_PERIOD = 120








#logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'main.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}