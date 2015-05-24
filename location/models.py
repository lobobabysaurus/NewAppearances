from django.db import models
from localflavor.us import models as us_models


class Location(models.Model):
    """
    A Location a user is coming from
    """
    street = models.CharField(max_length=255, blank=True, help_text="Street Address for a Location",)
    city = models.CharField(max_length=255, blank=True, help_text="City for a Location",)
    state = us_models.USStateField(blank=True, help_text="US State for a location",)
    zip = us_models.USZipCodeField(blank=True, help_text="Locations Zip Code",)
