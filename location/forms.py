from django.forms import ModelForm

from .models import Location


class LocationForm(ModelForm):
    """
    Location form based off of the Location model
    """
    class Meta:
        model = Location
        fields = ['street', 'city', 'state', 'zip']
