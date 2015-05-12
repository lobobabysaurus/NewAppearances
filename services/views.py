from django.shortcuts import render

from services.models import Service


def services_menu(request):
    """
    Default services view -  currently uses no model data
    TODO: Update services/models.py to include category images

    **Templates**

    :template:`products/products.html`

    :param request: Data send to the sever as part of a web request
    :return: A rendered blank services html file
    """
    return render(request, 'services/services.html')


def services(request, category_resource):
    """
    Get all services based on category and supply this list to the services/services.html template

    **Context**

    ``service_by_cat``
        Get all services as requested by category_resource from :model:`services.Service`

    **Templates**

    :template:`products/products.html`

    :param request: Data send to the sever as part of a web request
    :param category_resource: Name of the category of services to display
    :return: A html file rendered for the category
    """
    service_by_cat = Service.objects.filter(
        category=Service.category_reverse[category_resource.title()]).order_by('service_name')
    return render(request, 'services/services.html',
                  {'service_list': service_by_cat, 'category': category_resource.title()}, )
