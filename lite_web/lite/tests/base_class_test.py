from django.test import TestCase, Client


class MyTestSetting(TestCase):
    """
    Класс для общих данных
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
