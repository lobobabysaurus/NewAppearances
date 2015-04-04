from django.contrib import admin
from products.models import Brand, Product


class ProductInline(admin.StackedInline):
    """
    Have products be included with their brands
    """
    model = Product


class BrandAdmin(admin.ModelAdmin):
    """
    Have Brands display in a clean way
    """
    list_display = ('brandName', 'alt', 'isCarried', 'brandLogo',)
    inlines = [ProductInline]

admin.site.register(Brand, BrandAdmin)
