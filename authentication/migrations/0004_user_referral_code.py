# Generated by Django 4.2.5 on 2024-04-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_rename_full_name_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="referral_code",
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]