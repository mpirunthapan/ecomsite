from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name