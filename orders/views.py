from django.shortcuts import render


def index(request):
    return render(request, 'orders/orders_list.html')
