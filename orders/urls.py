from django.urls import path
from orders.apps import OrdersConfig
from orders.views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

app_name = OrdersConfig.name

urlpatterns = [
    #  urls для заказов:
    path('', OrderListView.as_view(), name='list'),
    path('details/<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
]
