# Generated by Django 5.0.3 on 2024-04-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('kg', 'Kg level'), ('E', 'Elementary level'), ('H', 'HighSchool level'), ('U', 'Undergraduate level'), ('M', 'Msc level'), ('P', 'Phd level')], max_length=100),
        ),
    ]
