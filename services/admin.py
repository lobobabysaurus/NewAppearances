from django.contrib import admin
from services.models import Service

# Register your models here.

"""
Have services dislay with service_name, minimum_cost, maximum_cost, and category for the admin view
"""
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'minimum_cost', 'maximum_cost', 'category',)

admin.site.register(Service, ServiceAdmin)