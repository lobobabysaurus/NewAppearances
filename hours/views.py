from django.shortcuts import render
from hours.models import Day


def hours(request):
    """
    Display the hours for every day of the week

    **Context**

    ``hoursList``
    All of the days of the week and their corresponding times from :model:`hours.Day`

    **Templates**

    :template:`hours/hours.html`
    """
    return render(request, "hours/hours.html", {'hoursList': Day.objects.order_by('dayName')},)