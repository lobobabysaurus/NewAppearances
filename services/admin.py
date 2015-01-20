from django.contrib import admin
from services.models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'minimum_cost', 'maximum_cost', 'category',)

admin.site.register(Service, ServiceAdmin)