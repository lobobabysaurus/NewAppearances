from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from services.models import Service

"""
Get all services and supply this list to the services/services.html template
"""
def services(request):
    all_services = Service.objects.order_by('order')

    return render(request, 'services/services.html', {'service_list': all_services,} )


