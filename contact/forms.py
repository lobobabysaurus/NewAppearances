from django import forms

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """
    Form definition to Contact the business
    """
    required_css_class = "contactFormField"
    error_css_class = "errorFormField"

    class Meta:
        """
        Link to the ContactSubmission model
        """
        model = ContactSubmission
        fields = ['sender', 'email', 'subject', 'message', ]
