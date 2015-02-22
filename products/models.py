from django.db import models

# Create your models here.

class Product(models.Model):

    alt = models.CharField(max_length=1000)
    isSold = models.BooleanField()
