from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Order, Product, Customer


class Command(BaseCommand):
    help = "Create customer."

    # def add_arguments(self, parser):
    #     parser.add_argument('customer', type=str, help='id customers')
    #     parser.add_argument('-products', type=list, default=[1, 2, 3, 4], help='--list id products')
    #
    # def handle(self, *args, **kwargs):
    #     total_price: float = 0
    #     product_set = set()
    #     product_list = kwargs['products']
    #     datetime = timezone.now()
    #     pk = kwargs.get('pk')
    #     customer = Customer.objects.filter(pk=pk).first()
    #     for pk in product_list:
    #         product = Product.objects.filter(pk=pk).first()
    #         total_price += product.price
    #         product_set.add(product)
    #     order = Order(customer=customer, products=product_set,
    #                   date_ordered=datetime, total_price=total_price)
    #     order.save()
    #     self.stdout.write(f'{order} created')

