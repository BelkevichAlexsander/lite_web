from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import VersionView


class TestUrlsTestCase(SimpleTestCase):
    def test_url_version(self):
        url = reverse('lite:version')
        self.assertEquals(resolve(url).func.view_class, VersionView)

    def test_url_version_pk(self):
        url = reverse('lite:version/pk', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, VersionView)
