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
MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

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
    'pynliner',
    'multiupload',
    'sorl.thumbnail',
    'support',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'tagging',
    'suit',
    'django.contrib.admin',
    'filebrowser',
    'tinymce',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# TINYMCE

TINYMCE_DEFAULT_CONFIG = {
    # General options
    'mode' : "textareas",
    'theme' : "advanced",
    'plugins' : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

    # Theme options
    'theme_advanced_buttons1' : "image,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,", #fullscreen,code",
    'theme_advanced_buttons2' : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,|,forecolor,backcolor",
    #'theme_advanced_buttons3' : "tablecontrols,|,hr,sub,sup,|,charmap",

    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : 'true',
    'file_browser_callback': 'filebrowser',

    #Example content CSS (should be your site CSS)
    #content_css : "/css/style.css",

    'template_external_list_url' : "lists/template_list.js",
    'external_link_list_url' : "lists/link_list.js",
    'external_image_list_url' : "lists/image_list.js",
    'media_external_list_url' : "lists/media_list.js",

    # Style formats
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'strong'},
        {'title' : 'Red text', 'inline' : 'span', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Help', 'inline' : 'strong', 'classes' : 'help'},
        {'title' : 'Table styles'},
        {'title' : 'Table row 1', 'selector' : 'tr', 'classes' : 'tablerow'}
    ],

    'width': '700',
    'height': '400'
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SENDER_EMAIL = 'schecksdavid@gmail.com'  # Mail qui envoie les mails
CONTACT_RECEIVER = 'schecksdavid@gmail.com' #Mail qui reçoit les contacts


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'schecksdavid@gmail.com'
EMAIL_HOST_PASSWORD = 'superskunk'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SITE_URL = "http://localhost:8001"



# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '13Atmosphere',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    'LIST_PER_PAGE': 15
}
