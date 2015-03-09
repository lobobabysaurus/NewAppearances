from django.shortcuts import render

from products.models import Brand

"""
Render a products page for all carried brands
"""
def products(request):
    return render(request, 'products/products.html', {"brandImages": Brand.objects.filter(isCarried=True)})