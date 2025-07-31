from django.test import SimpleTestCase
from django.urls import reverse


class HealthzPlainViewTest(SimpleTestCase):
    def test_healthz_plain_returns_200_and_ok(self):
        url = reverse("healthz")
        print(url)
        response = self.client.get(url)
        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "OK")
