from django.db import models
from django.utils import timezone


# Create your models here.


class Product(models.Model):
    order_number = models.IntegerField(default=0)
    price_usd = models.IntegerField(default=0)
    price_rub = models.IntegerField(default=0)
    delivery_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str("It's price: " + str(self.price_usd) + ", will be delivered: " + str(self.delivery_date))
