from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from rendertron.decorators.django import rendertron_render


def rendertron_mock_render(request, url=None):
    """
    Our mock Rendertron service for testing.
    :param request:
    :param str url: The url passed will be displayed in the response.
    :return:
    """
    html = b"""<html><body><p>Rendertron response for url: """
    html += bytes(url, "utf-8")
    html += b"""</p></body></html>"""
    return HttpResponse(content=html)


@rendertron_render
def decorated_view(request):
    """ A view function decorated with the @rendertron_render decorator. """
    html = b"""<html>
    <body>
        <p>Hello decorated view!</p>
    </body>
    </html>"""
    return HttpResponse(content=html)


def normal_view(request):
    """ A normal view function. Will only be rendered if the middleware is in place. """
    html = b"""<html>
    <body>
        <p>Hello normal view</p>
    </body>
    </html>"""
    return HttpResponse(content=html)


@method_decorator(rendertron_render, name="dispatch")
class DecoratedClassBasedView(View):
    """ A class based view decorated with the rendertron_render decorator. """

    def get(self, request):
        html = b"""<html>
        <body>
            <p>Hello class based view</p>
        </body>
        </html>"""
        return HttpResponse(content=html)
