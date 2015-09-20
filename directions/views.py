from django.http import JsonResponse
from django.shortcuts import render

from .models import Location
from .forms import DirectionForm


def directions(request):
    """
    Display the directions page

    **Context**

    ``form``
    Form display for the directions

    **Templates**

    :template:`directions/directions.html`

    :param request Data sent to the sever as part of a web request
    :return A directions finding form
    """
    return render(request, "directions/directions.html", {"form": DirectionForm()},)


def save_location(request):
    """
    Save or update the Location data a user has entered
    :param request The form data that was submitted by the user
    :return Json response containing the status of what happened in the request
    """
    response_json = {'status': "Not a post"}
    if request.method == "POST":
        try:
            # If the Location already exists, update the count on the database
            exist_check = Location.objects.get(street=request.POST['street'],
                                               city=request.POST['city'],
                                               state=request.POST['state'],
                                               zip=request.POST['zip'])
            exist_check.count += 1
            exist_check.save()
            response_json['status'] = "Count Updated"
        except Location.DoesNotExist:
            # If the Location doesn't already exist, save it
            locale = Location(street=request.POST['street'],
                              city=request.POST['city'],
                              state=request.POST['state'],
                              zip=request.POST['zip'])
            locale.save()
            response_json['status'] = "New Entry"
    return JsonResponse(response_json)
