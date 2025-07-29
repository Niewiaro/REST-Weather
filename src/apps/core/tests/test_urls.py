from django.urls import reverse, resolve
from django.test import SimpleTestCase
from apps.core.views.system import healthz, version, info


class CoreUrlsTest(SimpleTestCase):

    def test_healthz_url_resolves(self):
        url = reverse("healthz")
        self.assertEqual(resolve(url).func, healthz)

    def test_version_url_resolves(self):
        url = reverse("version")
        self.assertEqual(resolve(url).func, version)

    def test_info_url_resolves(self):
        url = reverse("info")
        self.assertEqual(resolve(url).func, info)
