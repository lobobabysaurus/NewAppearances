from django.contrib import admin
from hours.models import Day

"""
Admin display for hours
"""
class HoursAdmin(admin.ModelAdmin):
    list_display = ('dayName','startTime','endTime',)

admin.site.register(Day, HoursAdmin)