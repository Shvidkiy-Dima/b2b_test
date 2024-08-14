from rest_framework import serializers
from transaction.serializers import TransactionSerializer

from wallet.models import WalletModel


class WalletDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = WalletModel
        fields = ("id", "label", "balance", "transactions")


class WalletListSerializer(serializers.ModelSerializer):
    txs_count = serializers.IntegerField(read_only=True)
    balance = serializers.DecimalField(read_only=True, max_digits=18, decimal_places=2)

    class Meta:
        model = WalletModel
        fields = ("id", "label", "balance", "txs_count")
