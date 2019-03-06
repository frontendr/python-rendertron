import re

try:
    from django.conf import settings as django_settings
except ImportError:
    django_settings = None

# The url Rendertron is listening at.
RENDERTRON_BASE_URL = "http://localhost:3000"

# Query parameter added to requests made by Rendertron to be able to
# differentiate those from original requests.
RENDERTRON_RENDER_QUERY_PARAM = "rendertron_render"

# Storage settings
RENDERTRON_STORAGE = {
    "CLASS": "rendertron.storage.DummyStorage",
    "OPTIONS": {"TIMEOUT": 300},
}

# A list of patterns to include. When these match, excludes are not checked
RENDERTRON_INCLUDE_PATTERNS = []

# common static file extensions on the web
extensions = [
    "avi",
    "css",
    "flv",
    "gif",
    "ico",
    "jpe?g",
    "js",
    "less",
    "m4[av]",
    "mov",
    "mp[34]",
    "mpe?g",
    "pdf",
    "png",
    "rss",
    "svg",
    "swf",
    "ttf",
    "w[am]v",
    "woff2?",
    "xml",
]

# URL patterns to exclude from sending to Rendertron:
RENDERTRON_EXCLUDE_PATTERNS = [
    re.compile(r".*\.({ext})$".format(ext="|".join(extensions)))
]

if django_settings is not None:
    # Prepend Django's static paths:
    if getattr(django_settings, "STATIC_URL"):
        RENDERTRON_EXCLUDE_PATTERNS.insert(
            0, re.compile(r"^{url}".format(url=django_settings.STATIC_URL))
        )
    if getattr(django_settings, "MEDIA_URL"):
        RENDERTRON_EXCLUDE_PATTERNS.insert(
            0, re.compile(r"^{url}".format(url=django_settings.MEDIA_URL))
        )

# Extra patterns to exclude:
RENDERTRON_EXCLUDE_PATTERNS_EXTRA = []
