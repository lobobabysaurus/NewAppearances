from django.test import TestCase

from .models import HomePageText


class HomeTests(TestCase):
    """
    Learner for setting up a test
    """
    def testIsOneActiveText(self):
        """
        Trivial test to learn tests and make sure that an active home page text is active
        """
        active_text = HomePageText(is_active=True)
        self.assertEqual(active_text.is_active, True)
