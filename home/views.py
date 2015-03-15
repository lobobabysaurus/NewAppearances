from django.shortcuts import render

from home.models import HomePageText, HomePageImage

"""
Display the home page with associated content
"""
def home(request):
    # cast the active text and image to the template
    return render(request, 'home/home.html', {
        "homePageText": HomePageText.objects.get(isActive=True).pageText,
        "homePageImage": HomePageImage.objects.get(isActive=True).properImageURL,
        "imageAlt": HomePageImage.objects.get(isActive=True).alt,
    })