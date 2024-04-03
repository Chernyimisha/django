from django.shortcuts import HttpResponse, render
from django.utils import timezone
import logging
from dz2app.models import Customer, Order, Product

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def read_orders_customer(request, pk):
    customer = Customer.objects.filter(pk=pk).first()
    orders_qwery = Order.objects.filter(customer=customer).all()
    orders: dict = {}
    for order in orders_qwery:
        orders[order] = order.get_product().split('\n')
    context = {
        "customer": customer,
        "orders": orders,
    }
    return render(request, 'dz2app/index.html', context)


def read_orders_customer_by_days_by_order(request, pk):
    customer = Customer.objects.filter(pk=pk).first()
    orders_qwery = Order.objects.filter(customer=customer).all()
    orders_7_days: dict = {}
    orders_30_days: dict = {}
    orders_365_days: dict = {}
    current_date = timezone.now()

    for order in orders_qwery:
        if order.date_ordered >= current_date - timezone.timedelta(days=7):
            orders_7_days[order] = order.get_product().split('\n')
        elif order.date_ordered >= current_date - timezone.timedelta(days=30):
            orders_30_days[order] = order.get_product().split('\n')
        elif order.date_ordered >= current_date - timezone.timedelta(days=365):
            orders_365_days[order] = order.get_product().split('\n')

    context = {
        "customer": customer,
        "orders_7_days": orders_7_days,
        "orders_30_days": orders_30_days,
        "orders_365_days": orders_365_days,
    }

    return render(request, 'dz2app/orders_datesort_by_days_by_order.html', context)


def read_orders_customer_by_days(request, pk):
    customer = Customer.objects.filter(pk=pk).first()
    products_orders = []
    list_days = [7, 30, 365]

    for i in list_days:
        view_products_results = {}
        orders_qwery = Order.objects.filter(customer=customer,
                                            date_ordered__gte=timezone.now() - timezone.timedelta(days=i)).all()
        view_products = Order.get_product_set_orders(orders_qwery)
        products_orders.append(view_products.split('\n'))

    context = {
        "customer": customer,
        "products_7_days": products_orders[0],
        "products_30_days": products_orders[1],
        "products_365_days": products_orders[2],
    }

    return render(request, 'dz2app/orders_datesort_by_days.html', context)
