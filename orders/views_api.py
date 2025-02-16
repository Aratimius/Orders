"""
Отображение эндпоинтов для работы с API
"""

from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ('status', 'table_number',)  # Фильтрация по статусу или номеру стола
