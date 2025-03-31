from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import send_order_notification

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        send_order_notification(order.customer.phone_number, f"Order placed: {order.item} - {order.amount}")