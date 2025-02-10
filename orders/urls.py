from django.urls import path
from orders.apps import OrdersConfig
from orders.views import OrderListView

app_name = OrdersConfig.name

urlpatterns = [
    #  urls для заказов:
    path('', OrderListView.as_view(), name='list'),
    ]
