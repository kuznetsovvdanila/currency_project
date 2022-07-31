from __future__ import print_function

import os.path

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from datetime import date
from .models import Product, Dollar


def index(request):
    today_date = date.today()

    bucks = Dollar.objects.all()
    usd = Dollar()

    # checking if we have uploaded any usd value
    if not bucks:
        # if we haven't, getting it from the cbr's website
        usd.get_the_price()
        usd.save()
    else:
        # if we have, checking if the last usd value is valid
        if today_date != bucks[len(bucks) - 1].date:
            usd.get_the_price()
            usd.save()
        else:
            usd = bucks[len(bucks) - 1]

    products = Product.objects.all()
    if products:
        for i in range(len(products)):
            products[i].price_rub = round(products[i].price_usd * usd.price, 2)

    # necessary objects for the index page
    context = {
        'products': products,
        'usd': usd
    }
    return render(request, 'currency_app/index.html', context)
