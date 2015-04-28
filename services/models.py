from django.db import models

"""
Represents a service on the database

@field service_name Name of the providable service
@field minimum_cost Minimum cost of a range price service or base price of an & up services
@field maximum_cost Maximum cost of a range price service or price of a fixed price service
@field category_choices Mapping of constants to strings of service types so that we can save database space
@field order Value to order what services should appear where
"""
   
class Service(models.Model):
    #Constants to represent service types
    HAIRCUTS = 1
    COLORS = 2
    STRAIGHTENING = 3
    PERMS = 4
    SKINCARE = 5
    #Name of service, Primary key
    service_name = models.CharField(max_length=100, unique=True)
    #Minimum and maximum costs
    minimum_cost = models.IntegerField(blank=True, null=True)
    maximum_cost = models.IntegerField(blank=True, null=True)
    #Set up service catories
    category_choices = (
        (HAIRCUTS, 'haircuts'),
        (COLORS, 'colors'),
        (STRAIGHTENING, 'straightening'),
        (PERMS, 'perms'),
        (SKINCARE, 'skincare'),
    )
    category = models.IntegerField(choices=category_choices)
    
    #reverse key/value lookup
    category_reverse= {v: k for k, v in dict(category_choices).items()}
    
    #Set order in a modifiable display
    order = models.IntegerField(unique=True)
    
    def priceStr(self):
        if self.minimum_cost == None and self.maximum_cost != None:
            return (" $" + str(self.maximum_cost))
        elif self.minimum_cost != None and self.maximum_cost != None:
            return (" $" + str(self.minimum_cost) + " - $" + str(self.maximum_cost))
        elif self.minimum_cost != None and self.maximum_cost == None:
            return (" $" + str(self.minimum_cost) + " & up")
        else:
            return None