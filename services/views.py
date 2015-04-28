from django.shortcuts import render
from services.models import Service

"""
Get all services and supply this list to the services/services.html template
"""

#default services view -  currently uses no model data
#update services/models.py to include category images
def services_menu(request):
    return render(request, 'services/services.html')


#handles view for each service category
def services(request, category_resource):
    service = Service.objects.filter(category=Service.category_reverse[category_resource]).order_by('service_name')
    return render(request, 'services/services.html', {'service_list': service, 'category': category_resource.upper()}, )
