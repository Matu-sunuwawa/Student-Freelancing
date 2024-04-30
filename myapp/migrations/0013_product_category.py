# Generated by Django 5.0.3 on 2024-04-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_customeraddress_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('kg', 'Kg level'), ('E', 'Elementary level'), ('H', 'HighSchool level'), ('U', 'Undergraduate level'), ('M', 'Msc level'), ('P', 'Phd level')], default='Kg level', max_length=100),
        ),
    ]
