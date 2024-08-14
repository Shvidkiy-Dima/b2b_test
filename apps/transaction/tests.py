from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wallet.models import WalletModel

from transaction.models import TransactionModel


class TestTransaction(APITestCase):
    def test_rest_transaction(self):
        url_list = reverse("tx_list")

        wallet = WalletModel.objects.create(label="test")
        data = {"amount": Decimal("0.12"), "wallet_id": wallet.id, "txid": "test"}
        response = self.client.post(url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TransactionModel.objects.count(), 1)
        self.assertEqual(TransactionModel.objects.get().amount, data["amount"])
        self.assertEqual(TransactionModel.objects.get().wallet_id, data["wallet_id"])
        self.assertEqual(TransactionModel.objects.get().txid, data["txid"])

        url_detail = reverse("tx_detail", kwargs={"pk": response.json()["id"]})
        response = self.client.get(url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        assert str(response.json()["wallet_id"]) == str(data["wallet_id"])

        response = self.client.get(url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert len(response.json()["results"]) == 1
