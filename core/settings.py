"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jwwziwur^_p(a5nr5p-urs#aul52&d8#hs-uf@a!+2hq$fy@02'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    "dj_rest_auth",
    "dj_rest_auth.registration",

    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",

    "drf_yasg",
]

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_AUTHENTICATION_METHOD="email"
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_UNIQUE_EMAIL=True

AUTHENTICATION_BACKENDS=[
    # need to login by username un django admin, regardless of allauth
    "django.contrib.auth.backends.ModelBackend",
    # allauth specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend"
]

EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend"

REST_FRAMEWORK={
    # use Django's standard 'django.contrib.auth' presentation
    # or allow read-only access for unauthenticated users

    "DEFAULT_PERMISSION_CLASSES":[
        # rest_framework_simplejwt.authentication.JWTauthentication
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES":[
        # dj_rest_auth.jwt_auth.JWTCookieAuthentication
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
}

REST_AUTH={
    "USE_JWT":True,
    "JWT_AUTH_HTTPONLY":False,
    "JWT_AUTH_COOKIE": "core-app-auth",
    "KWT_AUTH_REFRESH_COOKIE": "core-refresh-token"
}

SIMPLE_JWT={
    "ACCESS_TOKEN_LIFETIME":timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=90)

}

SWAGGER_SETTINGS={
    "SECURITY_DEFINITIONS":{
        "Bearer":{"type":"apiKey","name":"Authorization", "in":"header"}
    }
}