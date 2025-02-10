from django.urls import path
from orders.apps import OrdersConfig
from orders.views import index


app_name = OrdersConfig.name

urlpatterns = [
    #  urls для заказов:
    path('', index),
    ]
