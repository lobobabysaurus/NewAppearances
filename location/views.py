from django.shortcuts import render


def location(request):
    """
    Display the location page

    **Templates**

    :template:`location/location.html`
    """
    return render(request, "location/location.html")