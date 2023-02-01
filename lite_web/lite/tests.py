from django.test import TestCase, Client
from django.urls import reverse

import json


class TestViewsDontCreate(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_project_list_GET(self):
        response = self.client.get('')

        self.assertEquals(response.status_code, 200)
        # self.assertJSONEqual(err)

    def test_project_list_POST(self):
        response = self.client.post('', {
            'software': 's1',
            'version': '1.2.3'
        })

        self.assertEquals(response.status_code, 200)
        # self.assertJSONEqual(err)

    def test_project_detail_GET(self):
        response = self.client.get('version/<int:lite_pk>/', args=[1])

        self.assertEquals(response.status_code, 404)
        # self.assertJSONEqual(err)
