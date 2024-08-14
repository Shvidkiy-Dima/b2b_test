from django.db.models import Count
from rest_framework import generics

from wallet.filters import WalletFilter
from wallet.models import WalletModel
from wallet.serializers import WalletDetailSerializer, WalletListSerializer


class WalletDetailView(generics.RetrieveAPIView):
    queryset = WalletModel.objects.prefetch_related("transactions")
    serializer_class = WalletDetailSerializer


class WalletListCreateView(generics.ListCreateAPIView):
    queryset = WalletModel.objects.annotate(txs_count=Count("transactions")).all()
    serializer_class = WalletListSerializer
    filterset_class = WalletFilter
