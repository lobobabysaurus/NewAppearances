from django.db import models

# Create your models here.
class HomePageText(models.Model):
    page_text = models.CharField(max_length=2500, null=True)
    is_active = models.BooleanField(default=False)
