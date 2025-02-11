from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from orders.forms import OrderCreateForm, OrderUpdateForm
from orders.models import Order


class OrderListView(ListView):
    """Отображение списка заказов"""

    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        """Подстчет выручки за все заказы"""

        context_data = super().get_context_data(**kwargs)
        proceeds: float = 0
        for order in Order.objects.all():
            proceeds += order.total_price

        context_data['proceeds'] = proceeds

        return context_data

    def get_queryset(self):
        """Реализация поиска заказа"""
        queryset = super().get_queryset()

        # ПОИСК ПО НОМЕРУ СТОЛА ИЛИ ПО СТАТУСУ ЗАКАЗА:
        search = self.request.GET.get("search", "")
        if search.isdigit():
            queryset = queryset.filter(Q(table_number=search))
            return queryset
        elif search:
            # ВНИМАНИЕ! Если поиск идет по статусу заказа, то вводить статус необходимо так:
            # WAITING, PAID или READY
            queryset = queryset.filter(Q(status=search))
            return queryset
        else:
            return queryset


class OrderDetailView(DetailView):
    """Детальный просмотр заказа"""

    model = Order

    def get_context_data(self, **kwargs):
        """Вынести в контекст блюда из заказа в отдельную переменную"""

        context_data = super().get_context_data(**kwargs)
        dishes = [item.name for item in Order.objects.get(pk=self.kwargs['pk']).items.all()]
        context_data['dishes'] = dishes

        return context_data


class OrderCreateView(CreateView):
    """Создание заказа"""

    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('orders:list')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderUpdateForm
    success_url = reverse_lazy('orders:list')


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:list')






