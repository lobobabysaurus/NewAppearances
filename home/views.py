from django.shortcuts import render

"""
Display the home page and associate content
"""
def home(request):
    #render the blank template for now
    return render(request, 'home/home.html')