from django.urls import path

from transaction import views

urlpatterns = [
    path("", views.TransactionListCreateView.as_view(), name="tx_list"),
    path("<uuid:pk>/", views.TransactionDetailView.as_view(), name="tx_detail"),
]
