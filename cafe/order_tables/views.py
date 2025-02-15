from django.shortcuts import render
from django.http import HttpResponse


def show_orders(request):
    return HttpResponse('Страница отображения заказов.')


def search_orders(request):
    return HttpResponse('Страница для осуществления поиска заказов.')


def change_status_orders(request):
    return HttpResponse('Страница для изменения статусов заказов.')


def create_orders(request):
    return HttpResponse('Страница для создания заказов.')


def delete_orders(request):
    return HttpResponse('Страница для удаления заказов.')


def show_profit(request):
    return HttpResponse('Страница для отображения прибыли.')
