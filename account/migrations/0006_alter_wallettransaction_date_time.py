# Generated by Django 5.0.2 on 2024-04-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_wallettransaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallettransaction",
            name="date_time",
            field=models.DateTimeField(),
        ),
    ]