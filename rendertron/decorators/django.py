from rendertron.middleware.django import DjangoRendertronMiddleware


def rendertron_render(view_func, **middleware_kwargs):
    """
    A Django view decorator to selectively apply `DjangoRendertronMiddleware`
    to a specific view.

    All keyword arguments are passed to the middleware.
    `include_patterns` and `exclude_patterns` are defaulted to an empty list
    because it makes no sense to have it for a specific view. You can still
    specify them for cases where your view serves responses that should be both
    rendered and not rendered.
    """

    middleware_kwargs.setdefault("include_patterns", [])
    middleware_kwargs.setdefault("exclude_patterns", [])

    def _wrapped_view_func(request, *args, **kwargs):
        def _get_response(request_from_middleware):
            return view_func(request_from_middleware, *args, **kwargs)

        middleware = DjangoRendertronMiddleware(_get_response, **middleware_kwargs)
        return middleware(request)

    return _wrapped_view_func
