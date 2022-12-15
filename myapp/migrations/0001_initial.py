# Generated by Django 4.1.4 on 2022-12-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="bulk_order",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("number", models.IntegerField()),
                ("address", models.CharField(max_length=200)),
                ("zip_code", models.IntegerField()),
                ("order_description", models.TextField()),
            ],
        ),
    ]
