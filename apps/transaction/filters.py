import django_filters

from transaction.models import TransactionModel


class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = TransactionModel
        fields = {
            "created_at": ("lt", "gt"),
            "modified_at": ("lt", "gt"),
            "amount": ("lt", "gt"),
            "txid": ("icontains",),
        }
