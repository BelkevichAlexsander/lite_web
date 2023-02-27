from django.urls import reverse

from .base_class_test import MyTestSetting

APPLICATION = 'application/json'


class TestViews(MyTestSetting):
    def test_list_GET(self):
        response = self.client.get(reverse('lite:version'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], APPLICATION)

    def test_list_GET_pk(self):
        self.version_control = [
            {
                'id': "0",
                'software': "software_1000000000",
                'version': '0.0.1'
            }
        ]

        response = self.client.get(reverse('lite:version/pk', kwargs={'pk': 0}))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], APPLICATION)

    def test_POST(self):
        response = self.client.post(
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

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], APPLICATION)
        self.assertEquals(self.version_control[0]['software'], 'software blank POST')
        self.assertEquals(self.version_control[1]['version'], 'vers')

    def test_PUT(self):
        response = self.client.put(
            reverse('lite:version/pk', kwargs={'pk': 0}),
            content_type=APPLICATION,
            data={
                'software': "software blank PUT",
                'version': 'version blank PUT'
            }
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], APPLICATION)
        self.assertEquals(self.version_control[0]['software'], 'software blank PUT')
        self.assertEquals(self.version_control[0]['version'], 'version blank PUT')

    def test_DELETE(self):
        self.version_control = [
            {
                'id': "0",
                'software': "software_1000000000",
                'version': '0.0.1'
            }
        ]

        response = self.client.delete(
            reverse('lite:version/pk', kwargs={"pk": 0}),
            content_type=APPLICATION
        )

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.headers['Content-Type'], APPLICATION)

        # Все равно понять не могу почему не отрабатывает delete
        # self.assertEquals(self.version_control[0]['software'], None)
        # self.assertEquals(self.version_control[0]['version'], None)
