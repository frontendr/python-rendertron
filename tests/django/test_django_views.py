from django.test import TestCase, override_settings
from django.urls import reverse


class DjangoTestCase(TestCase):
    @override_settings(ROOT_URLCONF="tests.django.urls")
    def test_decorated_view(self):
        response = self.client.get(reverse("decorated_view"))

        self.assertEqual(response.status_code, 200)
