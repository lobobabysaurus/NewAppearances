from django.contrib import admin
from products.models import Brand, Product

"""
Have products be included with their brands
"""
class ProductInline(admin.StackedInline):
    model = Product

"""
Have Brands display in a clean way
"""
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brandName', 'alt', 'isCarried', 'brandLogo',)
    inlines = [ProductInline]


admin.site.register(Brand, BrandAdmin)
