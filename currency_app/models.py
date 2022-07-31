from django.db import models
from django.utils import timezone
import pandas as pd


# Create your models here.


class Product(models.Model):
    order_number = models.IntegerField(default=0)
    price_usd = models.IntegerField(default=0)
    price_rub = models.IntegerField(default=0)
    delivery_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "It's price: " + str(self.price_usd) + ", will be delivered: " + str(self.delivery_date)


class Dollar(models.Model):
    price = models.DecimalField(default=0, max_digits=6, decimal_places=4)
    date = models.DateField(default=timezone.now())

    def get_the_price(self):
        # making "try finally" construction in order to exclude possible errors
        try:
            # getting the price of the usd value from cbr website, using pandas and numpy
            # 10 and 4 - are the rows and cols for the usd value in cbr's data table
            price_tmp = pd.read_html('https://www.cbr.ru/currency_base/daily/', decimal=',')[0].to_numpy()[10][4]
            # converting the price's format to a decimal
            self.price += price_tmp // 10000 + (price_tmp % 10000) * 0.0001
        finally:
            pass
        return self.price

    def __str__(self):
        return str(self.date) + ' usd price: ' + str(self.price)
