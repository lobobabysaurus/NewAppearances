from django.contrib import admin

from .models import Service, ServiceCategory, SubService


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
    list_editable = ('order',)
    ordering = ('category', 'order',)
    inlines = [ServiceInline]


class ServiceCategoryAdmin(admin.ModelAdmin):
    """
    Display categories for services
    """
    list_display = ('category_name', 'category_image', 'order')

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
