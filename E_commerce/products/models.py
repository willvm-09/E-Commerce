from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
     name = models.CharField(max_length=255, unique=True)

     def __str__(self):
          return self.name

# Validator function 
def price_check(price):
        if price < 0:
            raise ValidationError("Price Must be Equal to or Greater Than Zero")
        return price
        
class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[price_check])
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(max_length=500)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}'


# Order model that references the Product model. 
# Each order can contain multiple products, we'll assume each order contains a quantity of a single product.

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}"
    
    def stock_quantity_left(self, *args, **kwargs):
        if self.product.stock_quantity >= self.quantity:
              self.product.stock_quantity -= self.quantity
              self.product.save()
        else:
            raise ValidationError("Insufficient stock quantity!")
        super(Order, self).save(*args, **kwargs)
        
