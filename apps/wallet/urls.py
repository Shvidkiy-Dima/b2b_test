from django.urls import path

from wallet import views

urlpatterns = [
    path("", views.WalletListCreateView.as_view(), name="wallet_list"),
    path("<uuid:pk>/", views.WalletDetailView.as_view(), name="wallet_detail"),
]
