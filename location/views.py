from django.shortcuts import render

"""
Display the location page
"""
def location(request):
    return render(request, "location/location.html")