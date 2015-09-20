from django.test import TestCase

from .models import Service


class TestPriceStr(TestCase):
    """
    Test suite for Price string functionality
    """
    def testRangeString(self):
        """
        Tests the ranged display case
        """
        service = Service(minimum_cost=30, maximum_cost=40)
        self.assertEquals(service.price_str(), "$30 - $40", "Price range display not as expected")

    def testMaxString(self):
        """
        Checks the single value display case
        """
        service = Service(maximum_cost=40)
        self.assertEquals(service.price_str(), "$40", "Single value price display not as expected")

    def testMinString(self):
        """
        Checks the & up display case
        """
        service = Service(minimum_cost=30)
        self.assertEquals(service.price_str(), "$30 & up", "And Up display not as expected")

    def testNoString(self):
        """
        Checks the case of no prices set
        """
        service = Service()
        self.assertIsNone(service.price_str(), "No price display not as expected")
