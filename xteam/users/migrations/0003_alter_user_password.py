# Generated by Django 5.0.4 on 2024-04-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_age_alter_user_name_alter_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.BinaryField(),
        ),
    ]
