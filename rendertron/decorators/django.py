from django.utils.decorators import decorator_from_middleware_with_args

from rendertron.middleware.django import DjangoRendertronMiddleware


def rendertron_render(**kwargs):
    """
    A Django view decorator to selectively apply `DjangoRendertronMiddleware`
    to a specific view.

    All keyword arguments are passed to the middleware.
    """
    return decorator_from_middleware_with_args(DjangoRendertronMiddleware)(
        **kwargs
    )
