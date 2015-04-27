from django.contrib import admin

from contact.models import ContactForm


class ContactAdmin(admin.ModelAdmin):
    """
    Have previous  display in a clean way
    """
    list_display = ('sender', 'email', 'subject', 'message',)

admin.site.register(ContactForm, ContactAdmin)
