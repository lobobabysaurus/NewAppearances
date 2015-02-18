from django.contrib import admin
from django import forms
from home.models import HomePageText

# Register your models here.

class HomeTextForm(forms.ModelForm):
    page_text = forms.CharField(widget=forms.Textarea)

class HomeTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_text', 'is_active',]
    form = HomeTextForm

admin.site.register(HomePageText, HomeTextAdmin)
