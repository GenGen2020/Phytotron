"""
Django settings for login project.

Generated by 'django-user_admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(kz==a0un#orr7!*npdijwz7$x&4v1xx)4fhi7*^832h8^@^p^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "login.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "users/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'users.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

WSGI_APPLICATION = "login.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "phytotren",
        'USER': "root",
        'PASSWORD': "root",
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'CONN_MAX_AGE': 500,
        'POOL_SIZE': 100,
        'OPTIONS': {
            'charset': "utf8mb4",
            'isolation_level': None
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

AUTH_USER_MODEL = "users.CustomUser"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/users/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'users/static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'hdcyyg@126.com'
EMAIL_HOST_PASSWORD = 'XRDCHOIDLXFJLJNG'
EMAIL_USE_TLS = True


