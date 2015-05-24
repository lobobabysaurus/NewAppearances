from django.db import models


class ContactSubmission(models.Model):
    """
    Form through which a user can contact the business
    """
    sender = models.CharField(max_length=255, help_text="The name of the person who submitted a comment",)
    email = models.EmailField(max_length=255, help_text="The email of the person who submitted a comment",)
    subject = models.CharField(max_length=255, help_text="The message subject",)
    message = models.TextField(help_text="A user created message for the business",)
    time_sent = models.DateTimeField(auto_now_add=True, help_text="Time the submission was sent")

    def get_submission_email(self):
        """
        Takes the data that has been submitted and renders it into a human friendly emailable form
        :return: Descriptive message of what the end user communicated
        """
        new_section = "\r\n" * 2
        return "Message Sent by " + self.sender + " on " + str(self.time_sent) + new_section + \
            self.message + new_section + "If a response is necessary email " + self.email
