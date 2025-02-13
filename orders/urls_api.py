from rest_framework import routers
from orders.apps import OrdersConfig
from orders.views_api import OrderViewSet


app_name = OrdersConfig.name

router = routers.SimpleRouter()
router.register("", OrderViewSet)

urlpatterns = []

urlpatterns += router.urls
