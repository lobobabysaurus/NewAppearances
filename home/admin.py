from django.contrib import admin
from django import forms
from home.models import HomePageText, HomePageImage


"""
Set page to display in a full text area
"""
class HomeTextForm(forms.ModelForm):
    pageText = forms.CharField(widget=forms.Textarea)

"""
Show home data in a clean way
"""
class HomeTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'pageText', 'isActive',]
    form = HomeTextForm

"""
Have Brands display in a clean way
"""
class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'isActive', 'homeImage',)

admin.site.register(HomePageText, HomeTextAdmin)
admin.site.register(HomePageImage, HomeImageAdmin)