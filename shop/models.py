from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField()
    product_category = models.CharField(max_length=20)
    product_price = models.IntegerField()