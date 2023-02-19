from django.test import TestCase, Client

from ..views import VERSION_CONTROL


class MyTestSetting(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.version_control = VERSION_CONTROL
