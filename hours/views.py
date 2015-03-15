from django.shortcuts import render

"""
Display the hours page
"""
def hours(request):
    return render(request, "hours/hours.html")