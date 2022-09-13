import json

from django.test import TestCase, Client
from rest_framework import status

from .serializer import MobileSerializer
from .models import Mobile


client = Client()
url = "https://www.digikala.com/product/dkp-9092242/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a13-sm-a137fds-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/"


class GetAllPuppiesTest(TestCase):
    def test_single_product(self):
        response = client.post(
            data={"url": "%s" % url},
            path="/api/",
            content_type="application/json",
        )

        mobile = Mobile.objects.first()
        serializer = MobileSerializer(instance=mobile)

        self.assertEqual(json.loads(response.content), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_product_invalid_url(self):
        response = client.post(
            data=json.dumps('{"url":"vjraseilsjrrjrv"}'),
            path="/api/",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
