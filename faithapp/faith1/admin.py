from django.contrib import admin
from .models import Products, Customers, Orders, Suppliers
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Customers)
admin.site.register(Suppliers)
