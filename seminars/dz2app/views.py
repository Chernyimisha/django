from django.shortcuts import HttpResponse, render
from django.utils import timezone
import logging
from dz2app.models import Customer, Order, Product
from dz2app.forms import ProductForm, CustomerForm, OrderForm
from django.core.files.storage import FileSystemStorage
import json


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
        print(order)
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


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            volume = form.cleaned_data['volume']
            date = form.cleaned_data['date']
            product = Product(name=name, description=description, price=price, volume=volume)
            product.save()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Создан товар: {name=}, {price=}.')
            return HttpResponse(f"В базе сохранен товар: {product}")
    else:
        form = ProductForm()
        return render(request, 'dz2app/form.html', {'form': form})


def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            registration_date = form.cleaned_data['registration_date']
            customer = Customer(name=name, email=email, phone=phone, address=address)
            customer.save()
            logger.info(f'Создан клиент: {name=}, {email=}.')
            return HttpResponse(f"В базе сохранен клиент: {customer}")
    else:
        form = CustomerForm()
        return render(request, 'dz2app/form.html', {'form': form})


def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price: float = 0
            customer = form.cleaned_data['customer']
            products = form.cleaned_data['products']
            order = Order(customer=customer,
                          date_ordered=timezone.now(),
                          total_price=total_price)
            order.save()
            for product in products:
                order.products.add(product)
                total_price += product.price
                order.id_product_QUANTITY[product.pk] = 1
                product.volume -= 1
                product.save()
            order.total_price = total_price
            order.view_products = json.dumps(order.id_product_QUANTITY)
            order.save()
            logger.info(f'Создан заказ: #{order.pk}, на сумму {total_price}.')
            return HttpResponse(f"В базе сохранен заказ: {order}")
    else:
        form = OrderForm()
        return render(request, 'dz2app/form_order.html', {'form': form})
