from django.shortcuts import render
from hours.models import Day
"""
Display the hours page
"""
def hours(request):
    return render(request, "hours/hours.html", {'hoursList': Day.objects.all},)