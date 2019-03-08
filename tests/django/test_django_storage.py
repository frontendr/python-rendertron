from django.test import LiveServerTestCase
from django.urls import reverse


class DjangoStorageTestCase(LiveServerTestCase):
    def test_decorated_view_with_cache(self):
        """
        Test whether a view function decorated with @rendertron_render is rendered by
        the (mocked) Rendertron service. Then renders the same view again which should
        yield exactly the same result because it was cached.
        """
        with self.settings(
            ROOT_URLCONF="tests.django.urls",
            RENDERTRON_BASE_URL=self.live_server_url,
            # Enable a 'real' cache:
            RENDERTRON_STORAGE={
                "CLASS": "rendertron.storage.django.DjangoCacheStorage"
            },
        ):
            # get the view to fill storage:
            url = reverse("decorated_view")
            response = self.client.get(url)

            self.assertContains(response, "Rendertron response", status_code=200)

            # get the same url again and check if we get the cached result
            response2 = self.client.get(url)

            self.assertEqual(response.content, response2.content)
