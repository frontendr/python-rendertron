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

    def test_excluded_view_with_middleware(self):
        """
        Test whether an excluded view function is NOT rendered by the (mocked)
        Rendertron service if the `DjangoRendertronMiddleware` is in place.
        """
        with self.settings(
            # LiveServerTestCase starts a web server. self.live_server_url is it's URL.
            RENDERTRON_BASE_URL=self.live_server_url,
            RENDERTRON_EXCLUDE_PATTERNS=[r"^/excluded/"],
            ROOT_URLCONF="tests.django.urls",
            MIDDLEWARE=["rendertron.middleware.DjangoRendertronMiddleware"],
        ):
            response = self.client.get(reverse("excluded_view"))
            # It should not be rendered by our rendertron view:
            self.assertNotContains(response, "Rendertron response", status_code=200)
            self.assertContains(response, "normal view")

    def test_included_view_with_middleware(self):
        """
        Test whether an excluded view function is NOT rendered by the (mocked)
        Rendertron service if the `DjangoRendertronMiddleware` is in place.
        """
        with self.settings(
            # LiveServerTestCase starts a web server. self.live_server_url is it's URL.
            RENDERTRON_BASE_URL=self.live_server_url,
            # We exclude /excluded/
            RENDERTRON_EXCLUDE_PATTERNS=[r"^/excluded/"],
            # But include /excluded/included/ which should match first
            RENDERTRON_INCLUDE_PATTERNS=[r"^/excluded/included/"],
            ROOT_URLCONF="tests.django.urls",
            MIDDLEWARE=["rendertron.middleware.DjangoRendertronMiddleware"],
        ):
            response = self.client.get(reverse("included_view"))
            # It should not be rendered by our rendertron view:
            self.assertContains(response, "Rendertron response", status_code=200)
            self.assertNotContains(response, "normal view")
