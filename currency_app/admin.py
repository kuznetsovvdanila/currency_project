from django.contrib import admin

# Register your models here.


from .models import Product, Dollar

admin.site.register(Product)
admin.site.register(Dollar)
