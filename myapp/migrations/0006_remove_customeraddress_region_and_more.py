# Generated by Django 5.0.3 on 2024-04-23 07:57

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraddress',
            name='region',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='Product',
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='address',
            field=models.CharField(default='Street address', max_length=255),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 23, 7, 57, 2, 269942, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='email',
            field=models.EmailField(default='email@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customeraddress', to='myapp.order'),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customeraddress', to='myapp.customer'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem', to='myapp.product'),
        ),
    ]
