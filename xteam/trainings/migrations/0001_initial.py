# Generated by Django 5.0.4 on 2024-05-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0006_alter_user_subscription"),
    ]

    operations = [
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=300)),
                ("date", models.DateField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("img", models.CharField(max_length=200)),
                ("users", models.ManyToManyField(to="users.user")),
            ],
        ),
    ]