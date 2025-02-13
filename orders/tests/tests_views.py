"""
Тесты на контроллеры для модели Order
"""

from django.test import TestCase
from django.urls import reverse

from orders.models import Order, Dish


class OrderTestCase(TestCase):

    def setUp(self):
        """Создание объектов моделей Order и Dish для тестирования"""
        self.order = Order.objects.create(table_number=1)

        self.dish_1 = Dish.objects.create(name='Стейк Рибай', price=3000)
        self.dish_2 = Dish.objects.create(name='Стейк Медальон', price=2000)

        self.order.items.add(self.dish_1)
        self.order.items.add(self.dish_2)
        self.order.save()

    def test_order_detail(self):
        """Детальный просмотр"""

        url = reverse('orders:detail', args=(self.order.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.order)
        self.assertEqual(response.context['dishes'], ['Стейк Рибай', 'Стейк Медальон'])
        self.assertEqual(self.order.status, 'WAITING')

    def test_order_list(self):
        """Список заказов"""

        other_order = Order.objects.create(table_number=2)
        one_more_dish = Dish.objects.create(name='Стейк Флэнк', price=1000)
        other_order.items.add(one_more_dish)

        url = reverse('orders:list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['proceeds'], 0)  # Проверка корректности работы get_context_data
        self.assertEqual(len(response.context['order_list']), 2)

    def test_order_create(self):
        """Создание заказа"""

        url = reverse('orders:create')

        # Переход на страницу создания объекта
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Данные для создания нового объекта
        data = {
            'table_number': 3,
            'items': self.dish_1.pk
        }

        # Отправляем POST-запрос к CreateView
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)  # 302 - редирект после успешного создания
        self.assertEqual(Order.objects.filter(table_number=3).exists(), True)

    def test_order_update(self):
        """Обновление заказа"""

        url = reverse('orders:update', args=(self.order.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            'table_number': 5,
            'items': self.dish_1.pk,
            'status': 'PAID'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

        self.order.refresh_from_db()  # Обновление объекта из БД
        self.assertEqual(Order.objects.filter(table_number=5).exists(), True)
        self.assertEqual(len(Order.objects.all()), 1)
        self.assertEqual(self.order.total_price, 3000)
        self.assertEqual(self.order.status, 'PAID')

    def test_order_delete(self):
        """Удаление заказа"""

        url = reverse('orders:delete', args=(self.order.pk,))

        response = self.client.post(url)

        self.assertFalse(Order.objects.filter(pk=1).exists())
