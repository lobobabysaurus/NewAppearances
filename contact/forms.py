from django import forms

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """
    Form definition to Contact the business
    """
    error_css_class = "contactErrorField"
    required_css_class = "contactFormField"

    class Meta:
        """
        Link to the ContactSubmission model
        """
        model = ContactSubmission
        fields = ['sender', 'email', 'subject', 'message', ]
