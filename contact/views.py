from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    """
    Display the contact form and validate, save, and email on submit

    **Context**

    ``form``
    Django generated contact form

    **Templates**

    :template:`contact/contact.html`

    :param request Data sent to the sever as part of a web request
    :return A contact form on a failed submission or a success page if all required data is present
    """
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
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form, },)
