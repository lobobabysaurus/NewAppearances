from django.db import models


class Brand(models.Model):
    """
    Brands of products
    """
    brandName = models.CharField(max_length=255, unique=True,
                                 help_text="Name of the providable service should not have spaces",)
    alt = models.CharField(max_length=1000, help_text="Alternative text if the image cannot be displayed",)
    isCarried = models.BooleanField(default=True, help_text="Flag for if the product is being sold",)
    brandLogo = models.ImageField(upload_to='products/static/products/images',
                                  help_text="Image of the logo for the brand",)

    def properImageURL(self):
        """
        Shrinks the stored url to be the url django references during runtime
        """
        return self.brandLogo.url[len("products"):]


class Product(models.Model):
    """
    Individual Products
    """
    productName = models.CharField(max_length=255, unique=True, help_text="Name of the product",)
    productLink = models.CharField(max_length=1000, null=True, help_text="URL to the product page from provider",)
    productPrice = models.FloatField(null=True, help_text="Price of the Product",)
    productBrand = models.ForeignKey(Brand, related_name='products',
                                     help_text="Link to the brand which provides this product",)