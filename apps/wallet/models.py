from decimal import Decimal
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext as _

from utils.models import BaseModel


class WalletModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    label = models.CharField(max_length=124, verbose_name=_("Wallet label"))
    balance = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name=_("Wallet balance"), default=Decimal("0.00")
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(balance__gte=Decimal("0.00")), name="wallet_balance_gte_0"),
        ]
