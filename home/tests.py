from django.test import TestCase

from home.models import HomePageText


class HomeTests(TestCase):
    """
    Learner for setting up a test
    """
    def testIsOneActiveText(self):
        activeText = HomePageText(isActive=True)
        self.assertEqual(activeText.isActive, True)