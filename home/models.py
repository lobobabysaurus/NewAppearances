from django.db import models

"""
Shared fields between other Home Page Models

@field isActive Flag to determine if the text is the actively used home page text
"""
class HomePageModel(models.Model):
    isActive = models.BooleanField(default=False)

"""
Represents home page text on the database

@field pageText Text to be displayed on the home page
@field isActive Flag to determine if the text is the actively used home page text
"""
class HomePageText(HomePageModel):
    pageText = models.CharField(max_length=2500, null=True)

"""
Image for a home page

@field alt Alt text to include in the html
@field homePageImage Image of the logo for the brand
"""
class HomePageImage(HomePageModel):
    alt = models.CharField(max_length=1000)
    homeImage = models.ImageField(upload_to='home/static/home/images')

    """
    Shrinks the stored url to be the url django references while running
    @return shrunken url string
    """
    def properImageURL(self):
        return self.homePageImage.url[len("home"):]