from django import forms

from .models import ContactSubmission

# Placed outside of class because of issues with using in both ContactForm and nested Meta classes
form_fields_array = ['sender', 'email', 'subject', 'message', ]

class ContactForm(forms.ModelForm):
    """
    Form definition to Contact the business
    """
    required_css_class = "contactFormField"

    def __init__(self, *args, **kwargs):
        """
        Add the HTML5 required attribute to all of the fields
        """
        super().__init__(*args, **kwargs)
        for field_name in form_fields_array:
            self.fields[field_name].widget.attrs.update({"required": "True"})

    class Meta:
        """
        Link to the ContactSubmission model
        """
        model = ContactSubmission
        fields = form_fields_array