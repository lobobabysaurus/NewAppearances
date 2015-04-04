from django.contrib import admin
from hours.models import Day


class HoursAdmin(admin.ModelAdmin):
    """
    Display hours in a clean list
    """
    list_display = ('dayName','startTime','endTime',)

admin.site.register(Day, HoursAdmin)