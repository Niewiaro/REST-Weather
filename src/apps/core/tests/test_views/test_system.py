from rest_framework.test import APITestCase
from django.urls import reverse


class SystemViewTests(APITestCase):
    def test_healthz_ok(self):
        url = reverse("healthz-api")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "ok"})

    def test_healthz_allows_only_get(self):
        url = reverse("healthz-api")
        for method in ["post", "put", "delete", "patch"]:
            with self.subTest(method=method):
                response = getattr(self.client, method)(url)
                self.assertEqual(response.status_code, 405)

    def test_version_returns_expected_keys(self):
        url = reverse("version")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("version", response.data)
        self.assertIn("python", response.data)

    def test_version_allows_only_get(self):
        url = reverse("version")
        for method in ["post", "put", "delete", "patch"]:
            with self.subTest(method=method):
                response = getattr(self.client, method)(url)
                self.assertEqual(response.status_code, 405)

    def test_info_returns_expected_keys(self):
        url = reverse("info")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("app", response.data)
        self.assertIn("system", response.data)
        self.assertIn("hostname", response.data)
        self.assertIn("uptime", response.data)
        self.assertIn("database", response.data)
        self.assertIn("vendor", response.data["database"])
        self.assertIn("version", response.data["database"])

    def test_info_allows_only_get(self):
        url = reverse("info")
        for method in ["post", "put", "delete", "patch"]:
            with self.subTest(method=method):
                response = getattr(self.client, method)(url)
                self.assertEqual(response.status_code, 405)
