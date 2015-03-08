from django.db import models

"""
Represents home page text on the database

@field page_text Text to be displayed on the home page
@field is_active Flag to determine if the text is the actively used home page text
"""
class HomePageText(models.Model):
    page_text = models.CharField(max_length=2500, null=True)
    is_active = models.BooleanField(default=False)