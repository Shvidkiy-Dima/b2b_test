from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from wallet.models import WalletModel


class WalletTests(APITestCase):
    def test_rest_wallet(self):
        url_list = reverse("wallet_list")
        data = {
            "label": "test",
        }
        response = self.client.post(url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WalletModel.objects.count(), 1)
        self.assertEqual(WalletModel.objects.get().label, data["label"])

        url_detail = reverse("wallet_detail", kwargs={"pk": response.json()["id"]})
        response = self.client.get(url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.json()["label"] == data["label"]

        response = self.client.get(url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert len(response.json()["results"]) == 1
