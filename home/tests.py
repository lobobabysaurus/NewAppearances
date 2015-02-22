# Create your tests here.
from django.test import TestCase

from home.models import HomePageText

class HomeTests(TestCase):

    def testIsOneActiveText(self):
        """
        There should only be one active text returned
        :return:
        """
        activeText = HomePageText(is_active=True)
        self.assertEqual(activeText.is_active, True)