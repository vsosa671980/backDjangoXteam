# Generated by Django 5.0.4 on 2024-04-26 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0001_initial"),
        ("users", "0004_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="subscription",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="subscriptions.subscription",
            ),
        ),
    ]
