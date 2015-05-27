from django.shortcuts import render

from .forms import DirectionForm

def directions(request):
    """
    Display the directions page

    **Context**

    ``form``
    Form display for the directions

    **Templates**

    :template:`directions/directions.html`
    """
    return render(request, "directions/directions.html", {"form": DirectionForm()},)
