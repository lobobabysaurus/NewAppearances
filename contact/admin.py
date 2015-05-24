from django.contrib import admin

from contact.models import ContactSubmission


class ContactAdmin(admin.ModelAdmin):
    """
    Have previous  display in a clean way
    """
    list_display = ('sender', 'email', 'subject', 'message', 'time_sent',)

admin.site.register(ContactSubmission, ContactAdmin)
