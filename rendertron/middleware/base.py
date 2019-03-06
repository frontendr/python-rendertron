import re
from urllib.error import HTTPError

from urllib.request import urlopen
from urllib.parse import quote

from rendertron import default_settings
from rendertron.storage.base import get_storage


class RendertronMiddleware:
    def __init__(
        self,
        base_url=None,
        storage_settings=None,
        include_patterns=None,
        exclude_patterns=None,
    ):
        """
        Initializes the middleware by storing most arguments in the instance.
        :param str base_url: Base url of the Rendertron service.
        :param dict storage_settings: Settings for the storage class.
        :param list include_patterns: List of patterns to include.
        :param list exclude_patterns: List of patterns to exclude.
        """
        self.base_url = (base_url or default_settings.RENDERTRON_BASE_URL).rstrip("/")

        self.storage = get_storage(storage_settings)
        self.include_patterns = include_patterns or []
        self.exclude_patterns = exclude_patterns or []

    def is_excluded(self, path):
        """
        Checks if the given path is excluded from rendering
        :param str path: The path to check
        :rtype: bool
        """
        for include_pattern in self.include_patterns:
            if re.match(include_pattern, path):
                # When included we don't check excludes anymore
                return False

        for excluded_pattern in self.exclude_patterns:
            if re.match(excluded_pattern, path):
                return True
        return False

    def render_url(self, url, request):
        """
        Passes the given URL to the Rendertron service, reads the response,
        passes that to the storage and returns the response data.
        :param str url: The URL to be rendered by the Rendertron service.
        :param request: The request object which is passed to the storage.
        Varies per framework.
        :return: A tuple of response data and a metas dict
        :rtype: tuple
        """
        proxy_url = "{host}/render/{url}".format(host=self.base_url, url=quote(url))

        try:
            with urlopen(proxy_url) as response:
                if response.code == 200:  # What about other 'ok' codes?
                    data = response.read()
                    # Should we store the response code, headers etc?
                    metas = ["code", "reason", "status"]
                    meta = {key: getattr(response, key) for key in metas}
                    self.storage.store_response(request, data, meta)
                    return data, meta
        except HTTPError as e:
            # Should we raise/log errors?
            pass
        return None, None
