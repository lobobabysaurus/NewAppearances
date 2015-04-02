from django.shortcuts import render

from home.models import HomePageText, HomePageImage


def home(request):
    """
    Display the home page with associated image and text content

    **Context**

    ``homePageText``
        The active text from :model:`home.HomePageText`
    ``homePageImage``
        The active image from :model:`home.HomePageImage`
    ``imageAlt``
        Alt text for the active image

    **Template:**

    :template:`home/home.html`
    """
    return render(request, 'home/home.html', {
        "homePageText": HomePageText.objects.get(isActive=True).pageText,
        "homePageImage": HomePageImage.objects.get(isActive=True).properImageURL,
        "imageAlt": HomePageImage.objects.get(isActive=True).alt,
    })