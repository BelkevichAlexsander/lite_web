import json

from django.test import TestCase
from django.urls import reverse

from .base_class_test import MyTestSetting
from ..views import VERSION_CONTROL


class TestViews(MyTestSetting):
    def test_list_GET(self):
        response = self.client.get(reverse('lite:version'))
        self.assertEquals(response.status_code, 200)

    def test_list_GET_pk(self):
        VERSION_CONTROL.append(
            {
                'id': "0",
                'software': "software_1000000000",
                'version': '0.0.1'
            }
        )
        response = self.client.get(reverse('lite:version/pk', kwargs={'pk': 0}))
        self.assertEquals(response.status_code, 200)

    def test_POST(self):
        response = self.client.post('lite:version', data={
                                        'software': "software blank",
                                        'version': 'version blank'
                                    })

        print(response.status_code)
        print(dir(response))
        # print(response.body)
        # self.client.po
        # self.assertEquals(response.status_code, 302)

