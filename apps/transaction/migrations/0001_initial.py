# Generated by Django 5.1 on 2024-08-14 13:33

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionModel",
            fields=[
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "txid",
                    models.CharField(
                        db_index=True, editable=False, max_length=124, unique=True, verbose_name="Transaction id"
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=18, verbose_name="Transaction amount")),
                (
                    "wallet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="transactions",
                        to="wallet.walletmodel",
                        verbose_name="Transaction wallet",
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(("txid__length__gt", 0)), name="transaction_transactionmodel_txid_not_empty"
                    )
                ],
            },
        ),
    ]
