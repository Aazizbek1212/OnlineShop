from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='images/category', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    price = models.PositiveIntegerField()
    description = models.TextField()
    rating = models.FloatField()
    category = models.ForeignKey(Category, models.CASCADE, related_name='category', blank=True, null=True)

    def __str__(self):
        return self.name