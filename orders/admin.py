from django.contrib import admin

from orders.models import Order, Dish


@admin.register(Order)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'status', 'total_price',)


@admin.register(Dish)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
