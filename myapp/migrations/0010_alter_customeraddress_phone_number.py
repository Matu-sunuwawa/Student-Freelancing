# Generated by Django 5.0.3 on 2024-04-24 17:23

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]