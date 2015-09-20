from django.contrib import admin

from .models import Day


class HoursAdmin(admin.ModelAdmin):
    """
    Display hours in a clean list
    """
    list_display = ('day_name', 'start_time', 'end_time',)

admin.site.register(Day, HoursAdmin)
