import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

HERE = os.path.dirname(__file__)
SECRET_KEY = os.environ["EVENT_CREATOR_SECRET_KEY"]
ROOT_URLCONF = "event_creator.urls"

INSTALLED_APPS = (
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "event_creator",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase"
    }
}

OAUTH_CLIENT_ID = os.environ["EVENT_CREATOR_OAUTH_CLIENT_ID"]
OAUTH_CLIENT_SECRET = os.environ["EVENT_CREATOR_OAUTH_CLIENT_SECRET"]

AUTHENTICATION_BACKENDS = ("event_creator.auth.OAuth2AuthenticationBackend",
                           "django.contrib.auth.backends.ModelBackend")

AUTH_PROFILE_MODULE = "event_creator.UserProfile"

LOGIN_URL = "/login/"

STATIC_URL = '/static/'
