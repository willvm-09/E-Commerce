from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'category', 'stock_quantity')
    search_fields = ['name', 'category']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if min_price is not None and max_price is not None:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        return queryset

    def get(self, request):
        return Response({"message": "You are authenticated and can see this message!"})


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        return Response({"message": "You are authenticated and can see this message!"})
    
class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')
    search_fields = ['name']

    def get(self, request):
        return Response({"message": "You are authenticated and can see this message!"})




