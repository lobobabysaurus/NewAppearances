from django.shortcuts import render

from products.models import Brand


def products(request):
    """
    Render a products page for all carried brands

    **Context**

    ``brandImages``
        Set of all brand logos as defined in :model:`products.Brand`

    **Templates**

    :template:`products/products.html`
    """
    return render(request, 'products/products.html', {"brandImages": Brand.objects.filter(isCarried=True)})