from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    price = models.PositiveIntegerField()
    description = models.TextField()
    rating = models.FloatField()
