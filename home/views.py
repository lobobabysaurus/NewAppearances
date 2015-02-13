from django.shortcuts import render

from home.models import HomePageText
"""
Display the home page and associate content
"""
def home(request):
    #Get the active page text object
    activePageText = HomePageText.objects.get(is_active=True).page_text
    #cast the text to the tempalte
    return render(request, 'home/home.html', {"homePageText": activePageText})