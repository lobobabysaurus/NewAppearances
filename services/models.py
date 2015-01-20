from django.db import models

# Create your models here.


class Service(models.Model):
    #Constants to represent service types
    HAIRCUTS = 1
    COLORS = 2
    STRAIGHTENING = 3
    PERMS = 4
    SKINCARE = 5
    #Name of service, Primary key
    service_name = models.CharField(max_length=100, primary_key=True)
    #Minimum and maximum costs
    minimum_cost = models.IntegerField(blank=True, null=True)
    maximum_cost = models.IntegerField(blank=True, null=True)
    #Set up service catories
    category_choices = (
        (HAIRCUTS, 'Haircuts'),
        (COLORS, 'Colors'),
        (STRAIGHTENING, 'Straightening'),
        (PERMS, 'Perms'),
        (SKINCARE, 'Skincare'),
    )
    category = models.IntegerField(choices=category_choices)
    #Set order in a modifiable display
    order = models.IntegerField(unique=True)