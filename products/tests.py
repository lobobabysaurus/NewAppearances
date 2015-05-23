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
        test_image = Brand(brand_logo='products/static/products/images/testImage.jpg')
        self.assertEquals(test_image.proper_image_url(), "/static/products/images/testImage.jpg",
                          "URL not trimeed as expected")
