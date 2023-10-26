from django.contrib import admin
from .models import Products
from .models import Categories

class ProductsAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'size', 'in_stock']
  list_filter = ['in_stock']

admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)

