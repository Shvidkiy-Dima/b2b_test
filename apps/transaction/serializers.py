from decimal import Decimal
from typing import Dict, Optional
from uuid import UUID

from django.db import DatabaseError, transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from wallet.models import WalletModel

from transaction.models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    wallet_id = serializers.UUIDField()
    txid = serializers.CharField(validators=[UniqueValidator(queryset=TransactionModel.objects.all())])

    class Meta:
        model = TransactionModel
        fields = ("id", "txid", "wallet_id", "amount")

    def create(self, validated_data: Dict):
        wallet_id = validated_data.get("wallet_id")
        amount = validated_data.get("amount")
        with transaction.atomic():
            wallet = self._get_wallet(wallet_id=wallet_id)
            if wallet is None:
                raise serializers.ValidationError("Wallet not found")

            if Decimal("0.00") > wallet.balance + amount:
                raise serializers.ValidationError("Insufficient funds")

            tx = super().create({**validated_data, "wallet": wallet})
            wallet.balance += amount
            wallet.save()
            return tx

    def _get_wallet(self, wallet_id: UUID) -> Optional[WalletModel]:
        try:
            wallet = WalletModel.objects.select_for_update(nowait=True).filter(id=wallet_id).first()
        except DatabaseError:
            raise serializers.ValidationError("Blocked by the transaction")

        return wallet
