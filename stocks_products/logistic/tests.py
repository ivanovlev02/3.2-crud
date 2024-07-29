from unittest import TestCase

from rest_framework import APIClient


class MyTest(TestCase):
    def test_ok(self):

        def test_sample_view(self):
            url = "/api/v1/products"
            client = APIClient()
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
