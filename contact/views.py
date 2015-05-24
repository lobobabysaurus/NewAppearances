from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    """
    Display the contact form and validate, save, and email on submit

    **Context**

    ``form``
    Django generated contact form
    ``failed``
    Boolean if the form is being displayed after a failed submission attempt

    **Templates**

    :template:`contact/contact.html`
    """
    failed_attempt = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            fields = form.cleaned_data
            send_mail(fields['subject'],
                      contact_submission.get_submission_email(),
                      fields['email'],
                      ['newappearancesemail@gmail.com'],)
            return render(request, "contact/success.html",)
        else:
            failed_attempt = True
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form, "failed": failed_attempt},)
