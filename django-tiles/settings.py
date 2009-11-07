import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG


GMAP_API_KEY = 'fill_me_in' # this key does not need to be filled in when running locally.

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'postgresql_psycopg2'
#DATABASE_NAME = ''
#DATABASE_USER = ''
#DATABASE_PASSWORD = ''
#DATABASE_HOST = ''
#DATABASE_PORT = ''

TIME_ZONE = 'America/Vancouver'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

ROOT_PROJECT_FOLDER = os.path.dirname(__file__)


DISK_CACHE = os.path.join(ROOT_PROJECT_FOLDER,'cache')

MAPFILE_ROOT = os.path.join(ROOT_PROJECT_FOLDER,'mapfiles')

MAPNIK_MAPFILE = MAPFILE_ROOT + '/mapfile.xml'

MAPSERVER_MAPFILE = MAPFILE_ROOT + '/mapfile.map'

MEDIA_ROOT = os.path.join(ROOT_PROJECT_FOLDER,'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'vfnlvw6rlpevp)$w)8%5hgy67_aucgm9q)3coqqo-#3w$%gyxo'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PROJECT_FOLDER, 'templates'),
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.admin',
    #'django.contrib.humanize',
    #'registration',
    'tiles',
)

try:
    from local_settings import *
except ImportError, exp:
    pass
