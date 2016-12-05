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

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888',
]

SHELL_PLUS_PRE_IMPORTS = (
    ('blog.models', ('Post', 'myUser', 'Category', 'Tag', 'Rating',
                     'RatingPost','RatingTag','RatingUser','VotePost'
                     ,'UserVotes')),
    ('blog.functions', ('deleteThumb', 'srcsetThumb', 'findLink',
                        'findFile', 'saveImage','srcsets',)),
)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#EL_PAGINATION_LOADING = """<img src="/static/img/loader.gif" alt="loading" />"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*er@wzdwuga0)0u%j22+pthd0)wzgl%oka)+a^na37()xgr%f9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_URL='/login'

#FROALA_INCLUDE_JQUERY = False
FROALA_UPLOAD_PATH = str(datetime.date.today().year)+'/'\
+str(datetime.date.today().month)\
+'/'+str(datetime.date.today().day)+'/'

CACHEOPS_REDIS = {
    'host': '127.0.0.1', # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 1,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended

    'socket_timeout': 3,   # connection timeout in seconds, optional
    #'password': '...',     # optional
    'unix_socket_path': '/tmp/redis.sock' # replaces host and port
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    'auth.user': {'ops': 'get', 'timeout': 60*15},

    # Automatically cache all gets and queryset fetches
    # to other django.contrib.auth models for an hour
    'auth.*': {'ops': ('fetch', 'get'), 'timeout': 60*15},

    # Cache gets, fetches, counts and exists to Permission
    # 'all' is just an alias for ('get', 'fetch', 'count', 'exists')
    'auth.permission': {'ops': 'all', 'timeout': 60*15},

    # Enable manual caching on all other models with default timeout of an hour
    # Use Post.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic
    '*.*': {'ops': (), 'timeout': 60*15 },

    # And since ops is empty by default you can rewrite last line as:
    '*.*': {'timeout': 60*15},
}

ALLOWED_HOSTS = ['*']
DEBUG_TOOLBAR_PATCH_SETTINGS = False
JQUERY_URL = ""
SHOW_COLLAPSED = True
INTERNAL_IPS = ['192.168.1.68', '192.168.1.70', '127.0.0.1']

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'asmyshlyaev177@gmail.com'
EMAIL_HOST_PASSWORD = 'mypass'
DEFAULT_EMAIL_FROM = 'asmyshlyaev177@gmail.com'


SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email']
SOCIAL_AUTH_FACEBOOK_KEY = '1776776585908599'
SOCIAL_AUTH_FACEBOOK_SECRET = 'eb2bbc8be836f5f87c0c0c11eec821b0'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'name, email'
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1045385512187-plh57bf7ees9u12mg0obgo69lov7dje0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HmV6SyeDTrDOirzHkrCNZceK'
SOCIAL_AUTH_VK_OAUTH2_KEY = '5148734'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'jb2OnfWL2aCWns1hPSaP'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
#SOCIAL_AUTH_VK_APP_USER_MODE = 2
SOCIAL_AUTH_USER_MODEL = 'blog.myUser'
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
#SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    #'social.backends.google.GoogleOpenId',
    #'social.backends.google.GoogleOpenIdConnect',
    'blog.authentication.UsernameAuthBackend',
    'blog.authentication.EmailAuthBackend',

	'social.backends.facebook.FacebookOAuth2',
	'social.backends.vk.VKOAuth2',
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
    'django.contrib.staticfiles',
    #'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'blog',
    #'ckeditor',
    #'ckeditor_uploader',
    #'imagekit',
    'froala_editor',
    'compressor',
    'sorl.thumbnail',
    'django_cleanup',
    'django_celery_results',
    'social.apps.django_app.default',
    'django_extensions',
    #'django_pickling',
    'cacheops',
]

CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True
THUMBNAIL_PRESERVE_FORMAT = True

STATIC_URL = '/static/'
STATIC_ROOT = '/root/myblog/myblog/blog/static/'
MEDIA_ROOT = '/root/myblog/myblog/blog/static/media/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True # удобней выключить потом включу
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.rCSSMinFilter']
#IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.JustInTime'

#MIDDLEWARE = [  #for debug toolbar
MIDDLEWARE_CLASSES = [
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
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
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
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

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
