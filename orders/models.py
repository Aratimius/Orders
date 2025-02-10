"""
table_number (номер стола)
items (список заказанных блюд с ценами) - ДОПОЛНИТЕЛЬНАЯ МОДЕЛЬ
total_price (общая стоимость заказа, вычисляется автоматически) - ПОПРОБУЮ РЕАЛИЗОВАТЬ ЧЕРЕЗ ГЕТТЕР
status (статус заказа: “в ожидании”, “готово”, “оплачено”)
"""
from django.db import models


class Dish(models.Model):
    """Модель блюда"""

    name = models.CharField(max_length=200, verbose_name="Название блюда")
    price = models.FloatField(verbose_name="Цена в руб.")

    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "блюда"

    def __str__(self):
        return self.name


class Order(models.Model):
    """Модель заказа"""

    STATUS_CHOICES = (
        ("WAITING", "В ожидании"),
        ("READY", "Готово"),
        ("PAID", "Оплачено"),
    )

    table_number = models.PositiveIntegerField(verbose_name="Номер стола")
    status = models.CharField(
        default='WAITING',
        max_length=150,
        verbose_name="Статус заказа",
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
    )
    items = models.ManyToManyField(
        Dish,
        verbose_name="список блюд",
        related_name="orders",
        help_text="необходимо выбрать хотя бы одно блюдо из списка доступных",
    )

    @property
    def total_price(self):
        """Возвращаем полный прайс выбранных блюд"""
        total_price: float = 0
        for item in self.items.all():
            total_price += item.price
        return total_price

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
