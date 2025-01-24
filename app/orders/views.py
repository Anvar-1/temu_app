from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from app.products.models import Product

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        total_price = product.price * quantity  # Jami narx
        serializer.save(user=self.request.user, total_price=total_price)

        if serializer.validated_data['payment_method'] == 'card':
            card_number = serializer.validated_data.get('card_number')
            card_expiry = serializer.validated_data.get('card_expiry')

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]