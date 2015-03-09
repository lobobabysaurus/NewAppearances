from django.contrib import admin
from django import forms
from home.models import HomePageText


"""
Set page to display in a full text area
"""
class HomeTextForm(forms.ModelForm):
    page_text = forms.CharField(widget=forms.Textarea)

"""
Show home data in a clean way
"""
class HomeTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_text', 'is_active',]
    form = HomeTextForm

admin.site.register(HomePageText, HomeTextAdmin)
