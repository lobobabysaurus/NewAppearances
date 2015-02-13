from django.http import HttpResponse
from django.template import RequestContext, loader

from services.models import Service

"""
Get all services and supply this list to the services/services.html template
"""
def services(request):
    all_services = Service.objects.order_by('order')
    template = loader.get_template('services/services.html')

    context = RequestContext(request, {
        'service_list': all_services,
    })

    return HttpResponse(template.render(context))


