from django.test import TestCase

from services.models import Service


class TestPriceStr(TestCase):
    """
    Test suite for Price string functionality
    """
    def testRangeString(self):
        """
        Tests the ranged display case
        """
        service = Service(minimum_cost=30, maximum_cost=40)
        self.assertEquals(service.priceStr(), "$30 - $40")

    def testMaxString(self):
        """
        Checks the single value display case
        """
        service = Service(maximum_cost=40)
        self.assertEquals(service.priceStr(), "$40")

    def testMinString(self):
        """
        Checks the & up display case
        """
        service = Service(minimum_cost = 30)
        self.assertEquals(service.priceStr(), "$30 & up")

    def testNoString(self):
        """
        Checks the case of no prices set
        """
        service = Service()
        self.assertIsNone(service.priceStr())