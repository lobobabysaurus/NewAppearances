from django.shortcuts import render

from .models import Brand


def products(request):
    """
    Render a products page for all carried brands

    **Context**

    ``brandImages``
        Set of all brand logos as defined in :model:`products.Brand`

    **Templates**

    :template:`products/products.html`

    :param request Data sent to the sever as part of a web request
    :return A file containing all product related information
    """
    return render(request, 'products/products.html', {"brandImages": Brand.objects.filter(is_carried=True)})
