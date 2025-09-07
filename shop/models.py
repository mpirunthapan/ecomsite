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
    
class Order(models.Model):
    items = models.CharField(max_length=3000)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.CharField(max_length=200)

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.last_name}"