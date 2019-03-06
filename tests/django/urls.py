from django.urls import path, re_path

from tests.django import views

urlpatterns = [
    # This is our 'mock' Rendertron view:
    re_path("render/(?P<url>.*)$", views.rendertron_mock_render, name="mock_render"),
    # A 'normal' view, depends on middleware to be rendered by Rendertron
    path("normal/", views.normal_view, name="normal_view"),
    # A decorated view, should always be rendered by Rendertron
    path("decorated/", views.decorated_view, name="decorated_view"),
    # A class based view
    path(
        "class_based_view/",
        views.DecoratedClassBasedView.as_view(),
        name="class_based_view",
    ),
]
