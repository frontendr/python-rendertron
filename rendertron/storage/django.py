from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rendertron.storage.base import RendertronStorage


def get_cache_key(request):
    return "rendertron:{}".format(request.path)


class DjangoCacheStorage(RendertronStorage):
    """ A storage class that uses Django's cache as storage """

    @staticmethod
    def get_default_options():
        return {"TIMEOUT": DEFAULT_TIMEOUT, "VERSION": None}

    def get_stored_response(self, request):
        cache_key = get_cache_key(request)
        cached = cache.get(cache_key, default=None, version=self.options.get("VERSION"))
        if cached is not None:
            return cached["response"], cached["meta"]
        return None, None

    def store_response(self, request, response, meta):
        cache_key = get_cache_key(request)
        cache.set(
            cache_key,
            {"response": response, "meta": meta},
            timeout=self.options.get("TIMEOUT"),
            version=self.options.get("VERSION"),
        )
