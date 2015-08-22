from django.shortcuts import render

from .models import Service, ServiceCategory


def services_menu(request):
    """
    Default services view - display images for each category that map to each category specific page

    **Templates**

    :template:`services/serviceMenu.html`

    :param request: Data sent to the sever as part of a web request
    :return: An html file with picture representations of all services
    """
    categories = ServiceCategory.objects.order_by('order')
    return render(request, 'services/serviceMenu.html', {'categories': categories})


def services(request, category_resource):
    """
    Get all services based on category and supply this list to the services/services.html template

    **Context**

    ``service_by_cat``
        Get all services as requested by category_resource from :model:`services.Service`

    **Templates**

    :template:`services/services.html`

    :param request: Data sent to the sever as part of a web request
    :param category_resource: Name of the category of services to display
    :return: A html file rendered for the category
    """
    proper_cat = category_resource.title()
    service_by_cat = Service.objects.filter(
        category=Service.category_reverse[proper_cat]).order_by('order')
    return render(request, 'services/services.html',
                  {'service_list': service_by_cat, 'category': proper_cat}, )
