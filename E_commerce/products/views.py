from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return Response({"message": "You are authenticated and can see this message!"})


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        return Response({"message": "You are authenticated and can see this message!"})




