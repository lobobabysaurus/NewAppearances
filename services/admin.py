from django.contrib import admin
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    """
    Have services display in a clean way for the admin view
    """
    list_display = ('service_name', 'minimum_cost', 'maximum_cost', 'category', 'order',)

admin.site.register(Service, ServiceAdmin)