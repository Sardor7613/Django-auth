# Generated by Django 5.0.6 on 2024-06-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0015_subscription_features"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="subtitle",
            field=models.TextField(blank=True, null=True),
        ),
    ]
