from django.shortcuts import render

from .models import HomePageText, HomePageImage


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

    # Make sure there is data to back the image and text
    try:
        home_text = HomePageText.objects.get(is_active=True).page_text
    except HomePageText.DoesNotExist:
        home_text = None

    try:
        image_data = HomePageImage.objects.get(is_active=True)
        home_image = image_data.home_image
        image_alt = image_data.alt
    except HomePageImage.DoesNotExist:
        home_image = None
        image_alt = None

    return render(request, 'home/home.html', {
        "homePageText": home_text,
        "homePageImage": home_image,
        "imageAlt": image_alt,
    })
