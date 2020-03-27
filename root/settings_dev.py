import os
import mimetypes

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# The Django server is sloppy about mime types. Add what you need here.
mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
