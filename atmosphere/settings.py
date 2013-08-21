# Django settings for atmosphere project.
from settings_general import *
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'atmosphere_blog',                      # Or path to database file if using sqlite3.
        'USER': 'atmosphere',                      # Not used with sqlite3.
        'PASSWORD': 'labrador88',                  # Not used with sqlite3.
        'HOST': 'postgresql1.alwaysdata.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'l5q&amp;snr^scuj!^s9vlu8kbkr5$co04@_j3w@xnyu6h_j1hxvb6'
