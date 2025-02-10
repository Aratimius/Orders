from django.views.generic import ListView

from orders.models import Order


class OrderListView(ListView):
    """Эндпоинт для отображения списка заказов"""

    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        """Подстчет выручки за все заказы"""

        context_data = super().get_context_data(**kwargs)
        proceeds: float = 0
        for order in Order.objects.all():
            proceeds += order.total_price

        context_data['proceeds'] = proceeds

        return context_data
