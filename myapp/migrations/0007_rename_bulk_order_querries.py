# Generated by Django 4.1.4 on 2022-12-13 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_customers_password_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="bulk_order",
            new_name="Querries",
        ),
    ]