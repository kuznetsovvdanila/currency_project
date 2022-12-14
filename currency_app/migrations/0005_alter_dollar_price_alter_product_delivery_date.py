# Generated by Django 4.0.6 on 2022-07-31 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0004_dollar_alter_product_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollar',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 31, 9, 19, 58, 666114, tzinfo=utc)),
        ),
    ]
