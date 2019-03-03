from django.utils.decorators import decorator_from_middleware_with_args

from rendertron.middleware.django import DjangoRendertronMiddleware


def rendertron_render(**kwargs):
    """
    A Django view decorator to selectively apply `DjangoRendertronMiddleware`
    to a specific view.

    All keyword arguments are passed to the middleware.
    `include_patterns` and `exclude_patterns` are defaulted to an empty list
    because it makes no sense to have it for a specific view. You can still
    specify them for cases where your view serves responses that should be both
    rendered and not rendered.
    """
    return decorator_from_middleware_with_args(DjangoRendertronMiddleware)(
        include_patterns=kwargs.get('include_patterns', []),
        exclude_patterns=kwargs.get('exclude_patterns', []),
        **kwargs
    )
