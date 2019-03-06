from django.test import LiveServerTestCase
from django.urls import reverse


class DjangoTestCase(LiveServerTestCase):
    def test_decorated_view(self):
        """
        Test whether a view function decorated with @rendertron_render is rendered by
        the (mocked) Rendertron service.
        """
        with self.settings(
            ROOT_URLCONF="tests.django.urls", RENDERTRON_BASE_URL=self.live_server_url
        ):
            response = self.client.get(reverse("decorated_view"))
            self.assertContains(response, "Rendertron response", status_code=200)

    def test_class_based_view_with_decorator(self):
        """
        Test whether a class based view decorated with @rendertron_render is rendered by
        the (mocked) Rendertron service.
        """
        with self.settings(
            # LiveServerTestCase starts a web server. self.live_server_url is it's URL.
            RENDERTRON_BASE_URL=self.live_server_url,
            ROOT_URLCONF="tests.django.urls",
            MIDDLEWARE=["rendertron.middleware.DjangoRendertronMiddleware"],
        ):
            response = self.client.get(reverse("class_based_view"))
            self.assertContains(response, "Rendertron response", status_code=200)

    def test_normal_view_with_middleware(self):
        """
        Test whether a view function is rendered by the (mocked) Rendertron service if
        the `DjangoRendertronMiddleware` is in place.
        """
        with self.settings(
            # LiveServerTestCase starts a web server. self.live_server_url is it's URL.
            RENDERTRON_BASE_URL=self.live_server_url,
            ROOT_URLCONF="tests.django.urls",
            MIDDLEWARE=["rendertron.middleware.DjangoRendertronMiddleware"],
        ):
            response = self.client.get(reverse("normal_view"))
            self.assertContains(response, "Rendertron response", status_code=200)
