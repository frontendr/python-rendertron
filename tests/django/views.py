from django.http import HttpResponse

from rendertron.decorators.django import rendertron_render


@rendertron_render
def decorated_view(request):
    html = b'''<html>
    <body>
        <p>Hello world</p>
    </body>
    </html>'''
    return HttpResponse(content=html)
