from django.conf import settings
from django.http import HttpResponse

from rendertron import default_settings
from rendertron.middleware.base import RendertronMiddleware


def setting(name):
    """
    Returns the value of the setting by trying to get it from Django's settings
    object defaulting to the value in `default_settings`.
    :param str name: The name of the setting.
    """
    return getattr(settings, name, getattr(default_settings, name))


class DjangoRendertronMiddleware(RendertronMiddleware):
    """ Django specific middleware """

    def __init__(self, get_response, **kwargs):
        self.get_response = get_response

        # Should we move the query parameter logic to the super class?
        self.render_query_param = setting("RENDERTRON_RENDER_QUERY_PARAM")

        super(DjangoRendertronMiddleware, self).__init__(
            base_url=kwargs.get("base_url", setting("RENDERTRON_BASE_URL")),
            storage_settings=kwargs.get("storage", setting("RENDERTRON_STORAGE")),
            include_patterns=(
                kwargs.get("include_patterns", setting("RENDERTRON_INCLUDE_PATTERNS"))
            ),
            exclude_patterns=(
                kwargs.get(
                    "exclude_patterns",
                    setting("RENDERTRON_EXCLUDE_PATTERNS")
                    + setting("RENDERTRON_EXCLUDE_PATTERNS_EXTRA"),
                )
            ),
        )

    def get_rendered_response(self, request):
        """
        Forwards the given request to the Rendertron service and returns the
        response.
        :param django.http.HttpRequest request: The request to forward.
        :return: The response from the Rendertron service or None if it failed.
        :rtype: tuple
        """
        response, meta = self.storage.get_stored_response(request)
        if response is not None:
            return response, meta

        # Should we move the query parameter logic to the super class?
        url = "{url}?{param}=1".format(
            url=request.build_absolute_uri(), param=self.render_query_param
        )
        # Wouldn't it be awesome if we could move the rendering and storing
        # logic to a background process and first return the original response?
        return self.render_url(url, request)

    def requested_by_rendertron(self, request):
        """ Checks whether request originates from the Rendertron service. """
        # Should we move the query parameter logic to the super class?
        # Also, a header would be much nicer. Like 'x-renderer' in a response
        return self.render_query_param in request.GET

    def __call__(self, request):
        if not self.requested_by_rendertron(request) and not self.is_excluded(
            request.path
        ):
            # Get the rendered response
            content, meta = self.get_rendered_response(request)

            if content is not None:
                # possible keyword arguments of HttpResponse
                kwargs = ["content_type", "status", "reason", "charset"]
                return HttpResponse(
                    content=content, **{key: meta[key] for key in meta if key in kwargs}
                )

        # No rendered response was returned, continue as normal:
        response = self.get_response(request)
        return response
