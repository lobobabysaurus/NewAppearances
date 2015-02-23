from django.contrib import admin
from products.models import Product

# Register your models here.
"""
Have products display in a clean way
"""
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'alt', 'isSold', 'productImage',)

admin.site.register(Product, ProductAdmin)
