from django.contrib import admin
from services.models import Service


"""
Have services display in a clean way for the admin view
"""
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'minimum_cost', 'maximum_cost', 'category',)

admin.site.register(Service, ServiceAdmin)