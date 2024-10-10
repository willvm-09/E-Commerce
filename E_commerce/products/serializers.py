from rest_framework import serializers
from .models import Product
from .models import Order

#A serializer for the product model to handle validation and data transformation:

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero.')
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'order_date']

    def validate_quantity(self, data):
        product = data['product']
        order_quantity = data['quantity']

        if product.stock_quanity < order_quantity:
             raise serializers.ValidationError(f'Not enough stock for {product.name}. Only {product.stock_quantity} left in stock')
        return data
    
    def create(self, validated_data):
        product = validated_data['product']
        order_quantity = validated_data['quantity']
        product.stock_quantity -= order_quantity
        product.save()
        order = Order.objects.create(**validated_data)
        return order
    
