from django.test import TestCase

from services.models import Service

class TestPriceStr(TestCase):
    def testRangeString(self):
        service = Service(minimum_cost = 30, maximum_cost=40)
        self.assertEquals(service.priceStr(), "$30 - $40")

    def testMaxString(self):
        service = Service(maximum_cost=40)
        self.assertEquals(service.priceStr(), "$40")

    def testMinString(self):
        service = Service(minimum_cost = 30)
        self.assertEquals(service.priceStr(), "$30 & up")

    def testMinString(self):
        service = Service()
        self.assertIsNone(service.priceStr())