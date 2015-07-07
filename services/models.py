from django.db import models

class ServiceCategory(models.Model):
    """
    A category of services
    """
    category_name = models.CharField(max_length=55, unique=True, help_text="Name of the service category",)
    category_image = models.ImageField(upload_to="services/", help_text="Image to represent the category",)


class Service(models.Model):
    """
    A Service offered by the business
    """
    service_name = models.CharField(max_length=100, unique=True, help_text="Name of the providable service",)
    minimum_cost = models.IntegerField(blank=True, null=True,
                        help_text="Minimum cost of a range price service or base price of an & up services",)
    maximum_cost = models.IntegerField(blank=True, null=True,
                        help_text="Maximum cost of a range price service or price of a fixed price service",)
    order = models.IntegerField(help_text="Value to order what services should appear where")

    # Constants to represent service types
    HAIRCUTS = 1
    COLORS = 2
    STRAIGHTENING = 3
    PERMS = 4
    SKINCARE = 5
    category_choices = (
        (HAIRCUTS, 'Haircuts'),
        (COLORS, 'Colors'),
        (STRAIGHTENING, 'Straightening'),
        (PERMS, 'Perms'),
        (SKINCARE, 'Skincare'),
    )
    category = models.IntegerField(choices=category_choices,
                    help_text="Mapping of constants to strings of service types so that we can save database space",)
    # Reverse key/value lookup
    category_reverse = {category: cat_int for cat_int, category in dict(category_choices).items()}

    class Meta:
        """
        Defines composite unique key of category and order
        """
        unique_together = ('category', 'order',)

    def price_str(self):
        """
        Formats a string representing the price depending on minimum and maximum costs
        :return: $<max> if only a max is set, $<min>-$<max> if both are set and $<min> & up if only min is set
        """
        if self.minimum_cost is None and self.maximum_cost is not None:
            return "$" + str(self.maximum_cost)
        elif self.minimum_cost is not None and self.maximum_cost is not None:
            return "$" + str(self.minimum_cost) + " - $" + str(self.maximum_cost)
        elif self.minimum_cost is not None and self.maximum_cost is None:
            return "$" + str(self.minimum_cost) + " & up"
        else:
            return None


class SubService(models.Model):
    """
    Related statement or price for a service
    """
    text = models.CharField(max_length=255, help_text="Name of text to help another service",)
    price = models.IntegerField(blank=True, null=True, help_text="optional price",)
    service = models.ForeignKey(Service, related_name='sub_services',
                                help_text="Link to the service this addend",)
