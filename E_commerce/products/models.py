from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=200)
    stock_quantity = models.PositiveIntegerField()
    image = models.URLField(max_length=500)
    Created_Date = models.DateField(auto_now_add=True)

def __str__(self):
        return self.name

