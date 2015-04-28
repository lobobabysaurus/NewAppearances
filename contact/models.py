from django.db import models


class ContactForm(models.Model):
    """
    Form through which a user can contact the business
    """
    sender = models.CharField(max_length=255, blank=True, help_text="The name of the person who submitted a comment")
    email = models.EmailField(max_length=255, blank=True, help_text="The email of the person who submitted a comment")
    subject = models.CharField(max_length=255, blank=True, help_text="The message subject")
    message = models.TextField(help_text="A user created message for the business")