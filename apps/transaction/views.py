from rest_framework import generics

from transaction.filters import TransactionFilter
from transaction.models import TransactionModel
from transaction.serializers import TransactionSerializer


class TransactionDetailView(generics.RetrieveAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter
