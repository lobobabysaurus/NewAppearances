from django.test import TestCase

from products.models import Brand


class ProperURLTest(TestCase):
    """
    Test Brand image url manipulation
    """
    def testURLStripsProduct(self):
        """
        Test that stripping the initial section of the url functions properly
        """
        testImage = Brand(brandLogo='products/static/products/images/testImage.jpg')
        self.assertEquals(testImage.properImageURL(), "/static/products/images/testImage.jpg", "URL not trimeed as expected")