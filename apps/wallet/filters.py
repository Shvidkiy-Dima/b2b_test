import django_filters

from wallet.models import WalletModel


class WalletFilter(django_filters.FilterSet):
    class Meta:
        model = WalletModel
        fields = {
            "created_at": ("lt", "gt"),
            "modified_at": ("lt", "gt"),
            "balance": ("lt", "gt"),
            "label": ("icontains",),
        }
