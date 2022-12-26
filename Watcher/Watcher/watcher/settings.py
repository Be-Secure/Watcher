"""
Django settings for watcher project.

Generated by 'django-admin startproject' using Django 1.11.25.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import ldap
from django_auth_ldap.config import LDAPSearch

# LDAP Setup
AUTH_LDAP_SERVER_URI = os.environ.get('AUTH_LDAP_SERVER_URI', "")

# TLS/SSL Certificate Verification
AUTH_LDAP_VERIFY_SSL = os.environ.get('AUTH_LDAP_VERIFY_SSL', 'False')
if AUTH_LDAP_VERIFY_SSL == 'False':
    AUTH_LDAP_GLOBAL_OPTIONS = {ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER}

AUTH_LDAP_BIND_DN = os.environ.get('AUTH_LDAP_BIND_DN', "")
AUTH_LDAP_BIND_PASSWORD = os.environ.get('AUTH_LDAP_BIND_PASSWORD', "")

AUTH_LDAP_USER_SEARCH = LDAPSearch(os.environ.get('AUTH_LDAP_BASE_DN', ""),
                                   ldap.SCOPE_SUBTREE,
                                   os.environ.get('AUTH_LDAP_FILTER', "(uid=%(user)s)"))

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! You can set DJANGO_SECRET_KEY environment variable
# to change it within the .env file.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '9t4yzl@%fg*vd-@%jxn%e29v)j_pl_9-qu(onjic((jfca$z(!')
if SECRET_KEY == '':
    SECRET_KEY = '9t4yzl@%fg*vd-@%jxn%e29v)j_pl_9-qu(onjic((jfca$z(!'

# SECURITY WARNING: In production please put DJANGO_DEBUG environment variable to False in the .env file!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    os.environ.get('ALLOWED_HOST', '')
]

if os.environ.get('CSRF_TRUSTED_ORIGINS', '') != '':
    CSRF_TRUSTED_ORIGINS = [
        'https://' + os.environ.get('CSRF_TRUSTED_ORIGINS', ''),
        'http://' + os.environ.get('CSRF_TRUSTED_ORIGINS', '')
    ]

# threats_watcher APP settings
# Will use django-constance to store these settings in db

# Feed Parser Configuration
POSTS_DEPTH = 30
WORDS_OCCURRENCE = 10
# Example for daily watch : PostsDepth = 30 et WordsOccurrence = 5
# Example for a continuous watch : PostsDepth = 3 et WordsOccurrence = 8
# Example for a Monday morning watch : PostsDepth = 50 et WordsOccurrence = 0

# Email Configuration
EMAIL_FROM = os.environ.get('EMAIL_FROM', 'from@from.com')
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'localhost')
# Display at the end of the email notification
EMAIL_CLASSIFICATION = os.environ.get('EMAIL_CLASSIFICATION', 'Internal')
# Website url, link in e-mails body
WATCHER_URL = os.environ.get('WATCHER_URL', '')
# Watcher Logo
WATCHER_LOGO = os.environ.get('WATCHER_LOGO', 'https://raw.githubusercontent.com/thalesgroup-cert/Watcher/master'
                                              '/Watcher/static/Watcher-logo-simple.png')
# Proxy setup
HTTP_PROXY = os.environ.get('HTTP_PROXY', '')
HTTPS_PROXY = os.environ.get('HTTPS_PROXY', '')

# CertStream URL
CERT_STREAM_URL = os.environ.get('CERT_STREAM_URL', 'wss://certstream.calidog.io')

# Link to Searx Server API
DATA_LEAK_SEARX_URL = os.environ.get('DATA_LEAK_SEARX_URL', 'http://searx:8888/')

# The Hive Setup
THE_HIVE_URL = os.environ.get('THE_HIVE_URL', 'http://127.0.0.1:9000')
THE_HIVE_VERIFY_SSL = os.environ.get('THE_HIVE_VERIFY_SSL', False)
if THE_HIVE_VERIFY_SSL == "True":
    THE_HIVE_VERIFY_SSL = True
if THE_HIVE_VERIFY_SSL == "False":
    THE_HIVE_VERIFY_SSL = False
THE_HIVE_KEY = os.environ.get('THE_HIVE_KEY', '')
THE_HIVE_CASE_ASSIGNEE = os.environ.get('THE_HIVE_CASE_ASSIGNEE', 'watcher')
THE_HIVE_TAGS = os.environ.get('THE_HIVE_TAGS', "Watcher,Impersonation,Malicious Domain,Typosquatting").split(",")

# MISP Setup
MISP_URL = os.environ.get('MISP_URL', 'https://127.0.0.1')
MISP_VERIFY_SSL = os.environ.get('MISP_VERIFY_SSL', False)
if MISP_VERIFY_SSL == "True":
    MISP_VERIFY_SSL = True
if MISP_VERIFY_SSL == "False":
    MISP_VERIFY_SSL = False
MISP_KEY = os.environ.get('MISP_KEY', '')
MISP_TICKETING_URL = os.environ.get('MISP_TICKETING_URL', '')
MISP_TAGS = os.environ.get('MISP_TAGS', "Watcher,Impersonation,Malicious Domain,Typosquatting,TLP:Amber").split(",")

# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'threats_watcher',
    'rest_framework',
    'frontend',
    'data_leak',
    'site_monitoring',
    'dns_finder',
    'knox',
    'django.contrib.admindocs',
    'accounts',
    'import_export',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',)
}

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

ROOT_URLCONF = 'watcher.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'watcher.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# SECURITY WARNING: In production please set DB_USER and DB_PASSWORD environment variables in the .env file.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 3600,
        'NAME': 'db_watcher',
        'USER': os.environ.get('DB_USER', 'watcher'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'Ee5kZm4fWWAmE9hs'),
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.environ.get('TZ', 'Europe/Paris')

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
