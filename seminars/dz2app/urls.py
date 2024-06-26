from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.index, name='index'),
    path('orders/<int:pk>/', views.read_orders_customer, name='read orders from id customer'),
    path('orders_by_days_by_order/<int:pk>/', views.read_orders_customer_by_days_by_order, name='read orders from id customer'),
    path('orders_by_days/<int:pk>/', views.read_orders_customer_by_days, name='read orders from id customer'),
    path('form/product/', views.product_form, name='product form'),
    path('form/customer/', views.customer_form, name='customer form'),
    path('form/order/', views.order_form, name='order form'),
]

