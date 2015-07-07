from django.shortcuts import render

from .models import Day


def hours(request):
    """
    Display the hours for every day of the week

    **Context**

    ``hoursList``
    All of the days of the week and their corresponding times from :model:`hours.Day`

    **Templates**

    :template:`hours/hours.html`

    :param request Data sent to the sever as part of a web request
    :return A rendered hours file
    """
    return render(request, "hours/hours.html", {'hoursList': Day.objects.order_by('day_name')},)
