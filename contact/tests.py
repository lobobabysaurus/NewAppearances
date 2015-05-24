from datetime import datetime

from django.test import TestCase

from .models import ContactSubmission


class TestEmailMessage(TestCase):
    """
    Test automated generation of an email message
    """
    def testMessageGenerationAllFields(self):
        """
        Makes sure that a message generated matches what the expected output should be
        """
        submitted_form = ContactSubmission(sender="Yourself", message="Test Message",
                                           email="you@mirror.com", subject="Test Subject")
        time = datetime.now()
        submitted_form.time_sent = time
        generated_message = "Message Sent by Yourself on " + str(time) + "\r\n\r\nTest Message\r\n\r\n" + \
            "If a response is necessary email you@mirror.com"
        self.assertEqual(submitted_form.get_submission_email(), generated_message, "Message generated not as expected")
