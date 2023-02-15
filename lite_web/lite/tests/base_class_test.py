from django.test import TestCase, Client


class MyTestSetting(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

# не разноси специально для тестов оставил чтобы копировать код
        # VERSION_CONTROL = [
        #     {
        #         'id': "0",
        #         'software': "software_0",
        #         'version': '0.0.1'
        #     },
        #     {
        #         'id': "1",
        #         'software': "software_1",
        #         'version': '1.0.0'
        #     },
        #     {
        #         'id': "2",
        #         'software': "software_2",
        #         'version': '2.0.0'
        #     }
        # ]