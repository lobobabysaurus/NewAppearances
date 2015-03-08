from django.test import TestCase

from home.models import HomePageText

"""
Learner for setting up a test
"""
class HomeTests(TestCase):
    """
    There should only be one active text returned
    """
    def testIsOneActiveText(self):
        activeText = HomePageText(is_active=True)
        self.assertEqual(activeText.is_active, True)