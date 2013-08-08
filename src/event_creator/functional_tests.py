from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES["default"]["NAME"] = "functional_test"

OAUTH_REDIRECT_BASE = "http://localhost:8001"
