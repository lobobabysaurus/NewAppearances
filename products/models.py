from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=1000)
    alt = models.CharField(max_length=1000)
    isSold = models.BooleanField(default=True)
    productImage = models.ImageField(upload_to='products/static/images')

    def properURL(self):
        return self.productImage.url[len("products"):]
