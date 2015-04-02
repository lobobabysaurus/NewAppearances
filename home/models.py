from django.db import models


class HomePageModel(models.Model):
    """
    Fields to be used by other home page models
    """
    isActive = models.BooleanField(default=False, help_text="Flag to mark if the current item should be"
                                                            " displayed on the home page",)


class HomePageText(HomePageModel):
    """
    Text that is displayed on the home page of the site

    There should only be one set of home page text that is flagged as being active
    """
    pageText = models.CharField(max_length=2500, null=True, help_text="Text to display",)


class HomePageImage(HomePageModel):
    """
    Image to display on the home page

    There should only be one image that is flagged as being active

    """
    alt = models.CharField(max_length=1000, help_text="Alternative text if the image cannot be displayed",)
    homeImage = models.ImageField(upload_to='home/static/home/images', help_text="Image to display",)

    def properImageURL(self):
        """
        Shrinks the stored url to be the url django references during runtime
        """
        return self.homeImage.url[len("home"):]