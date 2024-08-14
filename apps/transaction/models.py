from uuid import uuid4

from django.db import models
from django.db.models.functions import Length
from django.utils.translation import gettext as _
from wallet.models import WalletModel

from utils.models import BaseModel

models.CharField.register_lookup(Length)


class TransactionModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    txid = models.CharField(
        max_length=124, editable=False, db_index=True, unique=True, verbose_name=_("Transaction id")
    )
    wallet = models.ForeignKey(
        WalletModel, verbose_name=_("Transaction wallet"), related_name="transactions", on_delete=models.RESTRICT
    )

    amount = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_("Transaction amount"))

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_txid_not_empty",
                check=models.Q(txid__length__gt=0),
            )
        ]
