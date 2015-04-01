from django.test import TestCase

from products.models import Brand

"""
Test Brand url manipulation
"""
class ProperURLTest(TestCase):
    """
    Test that stripping the initial section of the url functions properly
    """
    def testURLStripsProduct(self):
        testImage = Brand(brandLogo='products/static/products/images/testImage.jpg')
        self.assertEquals(testImage.properImageURL(), "/static/products/images/testImage.jpg", "URL not trimeed as expected")