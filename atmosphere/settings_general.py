# -*- coding:utf-8 -*-
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-FR'

ugettext = lambda s: s

MODELTRANSLATION_CUSTOM_FIELDS = ('HTMLField',)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_DEBUG = True
# DEFAULT_LANGUAGE = 1

LOCALE_PATHS = (
    os.path.join(PROJ_DIR, 'locale'),
)
LANGUAGES = (
	('fr', ugettext('Français')),
	('en', ugettext('Anglais')),
)

MODELTRANSLATION_TRANSLATION_FILES = (
    'blog.translation',
    'gallery.translation',
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'fr'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT = os.path.join(PROJ_DIR, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJ_DIR, 'static')

#deployment
SEND_BROKEN_LINK_EMAILS = True

MANAGERS = (
        ('webmaster', 'webmaster@13atmosphere.com'),
        ('david scheck', 'schecksdavid@gmail.com'),
    )

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



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
    'django.middleware.locale.LocaleMiddleware',
    'localeurl.middleware.LocaleURLMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'atmosphere.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'atmosphere.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJ_DIR, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'gallery',
    'blog',
    'atmosphere',
    'newsletter',
    'general_config',
    'pynliner',
    'multiupload',
    'sorl.thumbnail',
    'modeltranslation',
    'grappelli',
    'grappelli_modeltranslation',
    'grappelli.dashboard',
    'localeurl',
    'filebrowser',
    'compressor',
    'support',
    'tagging',
    'search',
    'outils',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)



POST_PER_PAGE = 10

GRAPPELLI_ADMIN_TITLE = "13Atmosphere"

TINYMCE_JS_URL = STATIC_URL +'grappelli/tinymce/jscripts/tiny_mce/'
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "grappelli/tiny_mce/jscripts/tiny_mce/")

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
TINYMCE_FILEBROWSER = True
# file_browser

import filebrowser
STATICFILES_DIRS += (os.path.join(os.path.dirname(filebrowser.__file__), 'static/'),)

ADMIN_MEDIA_PREFIX = '/media/admin/'

# URL_FILEBROWSER_MEDIA = ADMIN_MEDIA_PREFIX + 'filebrowser/'
FILEBROWSER_URL_TINYMCE = TINYMCE_JS_URL

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_STATIC_ROOT = STATIC_ROOT
FILEBROWSER_STATIC_URL = STATIC_URL
URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'
PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'

URL_TINYMCE = STATIC_URL + 'grappelli/jscripts/tiny_mce/'
PATH_TINYMCE = STATIC_ROOT + 'grappelli/jscripts/tiny_mce/'


FILEBROWSER_EXTENSIONS =  {
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
}


FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail','small', 'medium','big']
FILEBROWSER_ADMIN_THUMBNAIL = ('fb_thumb')


#compress
COMPRESS_ENABLED = False

DEFAULT_CONTENT_TYPE= 'text/html'

LOCALE_INDEPENDENT_PATHS = (
    r'^static/$',
)
