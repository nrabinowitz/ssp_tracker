# Django settings for ssp_tracker project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('nick', 'nick@nickrabinowitz.com'),
    ('rob', 'rrbaker@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # for development. XXX: Fill in server settings in local_settings.py
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tracker.db',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

ROOT_TEMPLATE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),"templates")

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_TEMPLATE_DIR, "static")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
# XXX: Override on in local_settings.py on server
SECRET_KEY = 'q-*#u1iwvsjs2ot3*p=-*1qyl$d9rhm@xbv%yec&1tvazw6wx$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ssp_tracker.urls'

TEMPLATE_DIRS = (
    ROOT_TEMPLATE_DIR,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'tracker',
    'south',
    'haystack',
    'django_filters',
)

HAYSTACK_SITECONF = 'ssp_tracker.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),"index")

# The following lines execute an optional local_settings.py file, which can override these settings
# either for development or for production vars (passwords, etc) we don't want in git
local_settings = os.path.normpath(os.path.join(os.path.dirname(__file__), 'local_settings.py').replace('\\','/'))
if os.path.exists(local_settings):
    execfile(local_settings)
