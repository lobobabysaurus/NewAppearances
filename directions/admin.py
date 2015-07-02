from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    """
    Display hours in a clean list
    """
    list_display = ('street', 'city', 'state', 'zip', 'count')

admin.site.register(Location, LocationAdmin)
