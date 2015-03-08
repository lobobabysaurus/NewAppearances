from django.contrib import admin
from products.models import Brand

"""
Have Brands display in a clean way
"""
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brandName', 'alt', 'isCarried', 'brandLogo',)

admin.site.register(Brand, ProductAdmin)
