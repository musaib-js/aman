# Generated by Django 4.1.4 on 2022-12-13 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_rename_bulk_order_querries"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Querries",
            new_name="Querry",
        ),
    ]
