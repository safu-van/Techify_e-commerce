# Generated by Django 5.0.2 on 2024-04-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0007_orders_payment_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="product_qty",
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
