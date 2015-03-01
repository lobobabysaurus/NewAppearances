from django.shortcuts import render

from products.models import Product
# Create your views here.

def products(request):
    return render(request, 'products/products.html', {"images": Product.objects.all})
