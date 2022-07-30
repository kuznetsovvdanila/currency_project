# Generated by Django 4.0.6 on 2022-07-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('order_number', models.IntegerField()),
                ('price_usd', models.IntegerField()),
                ('price_rub', models.IntegerField()),
                ('delivery_date', models.DateTimeField(verbose_name='date the product will be delivered')),
            ],
        ),
    ]