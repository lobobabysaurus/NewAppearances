from django.contrib import admin
from django import forms
from home.models import HomePageText, HomePageImage


class HomeTextForm(forms.ModelForm):
    """
    Show page text in a full text area
    """
    pageText = forms.CharField(widget=forms.Textarea)


class HomeTextAdmin(admin.ModelAdmin):
    """
    Have the possible home page texts display in a clean way
    """
    list_display = ['id', 'pageText', 'isActive',]
    form = HomeTextForm


class HomeImageAdmin(admin.ModelAdmin):
    """
    Have the possible home page Images display in a clean way
    """
    list_display = ('alt', 'isActive', 'homeImage',)

admin.site.register(HomePageText, HomeTextAdmin)
admin.site.register(HomePageImage, HomeImageAdmin)