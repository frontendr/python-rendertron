from django.urls import path

from tests.django import views

urlpatterns = [path("/decorated", views.decorated_view, name="decorated_view")]
