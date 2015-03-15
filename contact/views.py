from django.shortcuts import render

"""
Display the contact page
"""
def contact(request):
    return render(request, "contact/contact.html")