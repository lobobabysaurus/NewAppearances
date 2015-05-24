from django.shortcuts import render

from .forms import LocationForm

def location(request):
    """
    Display the location page

    **Context**

    ``form``
    Form display for the location

    **Templates**

    :template:`location/location.html`
    """
    return render(request, "location/location.html", {"form": LocationForm()},)
