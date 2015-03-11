from django.db import models

"""
Brands of products

@field bandName Name of the providable service, should not have spaces
@field alt Alt text to include in the html
@field isCarried Flag for if the product is being sold
@field brandLogo Image of the logo for the brand
"""
class Brand(models.Model):
    brandName = models.CharField(max_length=255, unique=True)
    alt = models.CharField(max_length=1000)
    isCarried = models.BooleanField(default=True)
    brandLogo = models.ImageField(upload_to='products/static/products/images')

    """
    Shrinks the stored url to be the url django references while running
    @return shrunken url string
    """
    def properImageURL(self):
        return self.brandLogo.url[len("products"):]

"""
Individual Products

@field productName Name of the product, should not have spaces
@field productLink URL to the product page
@field productPrice Price of the Product
@field productBrand Link to the brand this product belongs to
"""
class Product(models.Model):
    productName = models.CharField(max_length=255, unique=True)
    productLink = models.CharField(max_length=1000, null=True)
    productPrice = models.FloatField(null=True)
    productBrand = models.ForeignKey(Brand, related_name='products')