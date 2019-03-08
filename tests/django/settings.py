CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
DEBUG = True
INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
SECRET_KEY = "secret-key-purely-for-running-tests"
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
TEST_RUNNER = "tests.django.runner.NoDBTestRunner"
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "django-test.db"}
}
STATIC_URL = "/static/"  # required: https://code.djangoproject.com/ticket/28235
