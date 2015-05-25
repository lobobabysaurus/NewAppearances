from django.contrib import admin

from services.models import Service, SubService


class ServiceInline(admin.StackedInline):
    """
    Have sub service text be included with their services
    """
    model = SubService


class ServiceAdmin(admin.ModelAdmin):
    """
    Have services display in a clean way for the admin view
    """
    list_display = ('service_name', 'minimum_cost', 'maximum_cost', 'category', 'order',)
    inlines = [ServiceInline]

admin.site.register(Service, ServiceAdmin)
