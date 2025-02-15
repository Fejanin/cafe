from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_orders, name='show_orders'),
    path('search_orders/', views.search_orders, name='search_orders'),
    path('change_status_orders/', views.change_status_orders, name='change_status_orders'),
    path('create_orders/', views.create_orders, name='create_orders'),
    path('delete_orders/', views.delete_orders, name='delete_orders'),
    path('show_profit/', views.show_profit, name='show_profit'),
]
