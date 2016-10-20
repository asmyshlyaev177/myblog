"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import datetime
from django.utils import timezone

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#EL_PAGINATION_LOADING = """<img src="/static/img/loader.gif" alt="loading" />"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*er@wzdwuga0)0u%j22+pthd0)wzgl%oka)+a^na37()xgr%f9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#today = datetime.date.today()
summernote_filepath = str(datetime.date.today().year)+'/'\
+str(datetime.date.today().month)\
+'/'+str(datetime.date.today().day)+'/'
SUMMERNOTE_CONFIG = {
    'iframe': False,
    'lang': 'ru-RU',
    'width': '100%',
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video', 'hr']],
        ['view', ['fullscreen']],

    ],
    'attachment_require_authentication': True,
    'disable_upload': False,
    'attachment_upload_to': summernote_filepath,
    'internal_js': (
        ('/static/django_summernote/jquery.ui.widget.js'),
        ('/static/django_summernote/jquery.iframe-transport.js'),
        ('/static/django_summernote/jquery.fileupload.js'),
        ('/static/django_summernote/summernote.min.js'),
    ),

    # You can add custom css/js for SummernoteWidget.
    'css': (
    ),
    'js': (
        ('/static/django_summernote/lang/summernote-ru-RU.min.js'),
    ),
    }


ALLOWED_HOSTS = ['*']
DEBUG_TOOLBAR_PATCH_SETTINGS = False
JQUERY_URL = ""
SHOW_COLLAPSED = True
INTERNAL_IPS = ['192.168.1.68', '192.168.1.70', '127.0.0.1']

LOGIN_REDIRECT_URL = '/dashboard'

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'asmyshlyaev177@gmail.com'
EMAIL_HOST_PASSWORD = 'mypass'
DEFAULT_EMAIL_FROM = 'asmyshlyaev177@gmail.com'

AUTHENTICATION_BACKENDS = (
    'blog.authentication.UsernameAuthBackend',
    'blog.authentication.EmailAuthBackend',
)

AUTH_USER_MODEL = 'blog.myUser'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
# Application definition

INSTALLED_APPS = [
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    #'ckeditor',
    #'ckeditor_uploader',
    'imagekit',
    'django_summernote',
    'compressor',
]

STATIC_URL = '/static/'
STATIC_ROOT = '/django/python3/myblog/blog/static/'
MEDIA_ROOT = '/django/python3/myblog/blog/static/media/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = False  # удобней выключить потом включу
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.rCSSMinFilter']
IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.JustInTime'

#CKEDITOR_JQUERY_URL = '///static/js/jquery-latest.js"'
#CKEDITOR_UPLOAD_PATH = 'uploads/'
#CKEDITOR_IMAGE_BACKEND = 'pillow'
#CKEDITOR_RESTRICT_BY_USER = True
#CKEDITOR_BROWSE_SHOW_DIRS = True

'''CKEDITOR_CONFIGS = {
    "post": {
        "toolbar": [
            { 'name': 'undo_redo', 'items': ["Undo", "Redo", "-", "Preview"]},
            '/',
            { 'name': 'style', 'items': ['Format', "Bold", "Italic", "Underline",
                                     "Strike", "Blockquote"]},
            ["NumberedList", "BulletedList", "-", "JustifyLeft", "JustifyCenter",
              "JustifyRight", "JustifyBlock"],
            '/',
            ["Link", "Unlink"],["Table", "Image", "Youtube"]
        ],
        "removePlugins": "flash",
        "extraPlugins": ','.join(["autogrow",
                        "youtube", "preview"])
    },
    "description": {
        "toolbar": [
            { 'name': 'undo_redo', 'items': ["Undo", "Redo"]},
            { 'name': 'style', 'items': ["Bold", "Italic", "Underline",
                                     "Strike", "Blockquote"]},
            ["NumberedList", "BulletedList", "-", "JustifyLeft", "JustifyCenter",
              "JustifyRight", "JustifyBlock"],
            ["Table"]
        ],
        "removePlugins": "flash",
        "extraPlugins": ','.join(["autogrow",
                        "youtube", "preview"])

    }
}'''

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
