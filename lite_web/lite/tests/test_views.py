from django.urls import reverse

from .base_class_test import MyTestSetting
from ..views import VERSION_CONTROL

APPLICATION = 'application/json'


class TestViews(MyTestSetting):
    def test_list_GET(self):
        self.client.post(reverse('lite:version'),
                         data={
                             'software': "first GET no pk",
                             'version': 'first GET no pk'
                         })

        self.assertEquals(VERSION_CONTROL[len(VERSION_CONTROL) - 1]['software'],
                          "first GET no pk")
        self.assertEquals(VERSION_CONTROL[len(VERSION_CONTROL) - 1]['version'],
                          "first GET no pk")

    def test_list_GET_pk(self):
        self.client.post(reverse('lite:version'),
                         data={
                             'software': "second GET with pk",
                             'version': 'second GET with pk'
                         })
        index_get_pk = len(VERSION_CONTROL) - 1
        response = self.client.get(reverse('lite:version/pk',
                                           kwargs={
                                               'pk': index_get_pk
                                           }))

        self.assertEquals(VERSION_CONTROL[index_get_pk]['software'], 'second GET with pk')

    def test_POST(self):
        self.client.post(
            reverse('lite:version'),
            data={
                'software': "software blank POST",
                'version': 'version blank POST'
                }
        )

        self.client.post(
            reverse('lite:version'),
            data={
                'software': "soft",
                'version': 'vers'
            }
        )

        index_post = len(VERSION_CONTROL) - 1

        self.assertEquals(VERSION_CONTROL[index_post - 1]['software'], 'software blank POST')
        self.assertEquals(VERSION_CONTROL[index_post]['version'], 'vers')

    def test_PUT(self):
        self.client.post(
            reverse('lite:version'),
            data={
                'software': "ADD POST IN PUT-test",
                'version': 'ADD POST IN PUT-test'
            }
        )

        self.client.put(
            reverse('lite:version/pk', kwargs={'pk': 0}),
            content_type=APPLICATION,
            data={
                'software': "software blank PUT",
                'version': 'version blank PUT'
            }
        )

        self.assertEquals(VERSION_CONTROL[0]['software'], 'software blank PUT')
        self.assertEquals(VERSION_CONTROL[0]['version'], 'version blank PUT')

    def test_DELETE(self):
        self.client.post(
            reverse('lite:version'),
            data={
                'software': "ADD POST IN DELETE-test",
                'version': 'ADD POST IN DELETE-test'
            }
        )

        self.client.delete(
            reverse('lite:version/pk', kwargs={"pk": 0}),
            content_type=APPLICATION
        )

        self.assertEquals(VERSION_CONTROL[0]['software'], None)
        self.assertEquals(VERSION_CONTROL[0]['version'], None)
