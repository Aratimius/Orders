from rest_framework.serializers import ModelSerializer
from orders.models import Order, Dish


class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = ('name', 'price',)


class OrderSerializer(ModelSerializer):

    items = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
