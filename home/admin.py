from django import forms
from django.contrib import admin

from .models import HomePageText, HomePageImage


class HomeTextForm(forms.ModelForm):
    """
    Show page text in a full text area
    """
    page_text = forms.CharField(widget=forms.Textarea)


class HomeTextAdmin(admin.ModelAdmin):
    """
    Have the possible home page texts display in a clean way
    """
    list_display = ['id', 'page_text', 'is_active', ]
    form = HomeTextForm


class HomeImageAdmin(admin.ModelAdmin):
    """
    Have the possible home page Images display in a clean way
    """
    list_display = ('alt', 'is_active', 'home_image',)

admin.site.register(HomePageText, HomeTextAdmin)
admin.site.register(HomePageImage, HomeImageAdmin)
