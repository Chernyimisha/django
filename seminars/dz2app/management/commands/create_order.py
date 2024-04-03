import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Order, Product, Customer
import json
from random import choices, randint


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument('customer', type=int, help='id customers')
        parser.add_argument('-products', type=list,
                            default=choices([randint(1, 11), 1, 2, 3, 4, 5, randint(1, 10)], k=randint(1, 6)),
                            help='--list id products')

    def handle(self, *args, **kwargs):
        total_price: float = 0
        product_list = set(kwargs['products'])
        pk = kwargs['customer']
        customer = Customer.objects.filter(pk=pk).first()
        order = Order(customer=customer,
                      date_ordered=timezone.now() - timezone.timedelta(days=choices([3, 15, 40, 380])[0]),
                      total_price=total_price)
        order.save()

        for pk in product_list:
            product = Product.objects.filter(pk=pk).first()
            count_same_product = kwargs['products'].count(pk)
            product_price = product.price * count_same_product
            total_price += product_price
            order.products.add(product)
            order.id_product_QUANTITY[pk] = count_same_product
            product.volume -= count_same_product
            product.save()

        order.total_price = total_price
        order.view_products = json.dumps(order.id_product_QUANTITY)
        order.save()
        self.stdout.write(f'{order}')
