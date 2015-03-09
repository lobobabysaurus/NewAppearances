from django.shortcuts import render

from home.models import HomePageText

"""
Display the home page with associated content
"""
def home(request):
    #cast the acive text to the template
    return render(request, 'home/home.html', {"homePageText": HomePageText.objects.get(is_active=True).page_text})