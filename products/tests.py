from django.test import TestCase

from products.models import Product

# Create your tests here.

class ProperURLTest(TestCase):

    def testURLStripsProduct(self):
        testImage = Product(productImage='products/static/products/images/testImage.jpg')
        self.assertEquals(testImage.properURL(), "/static/products/images/testImage.jpg","URL not trimeed as expected")