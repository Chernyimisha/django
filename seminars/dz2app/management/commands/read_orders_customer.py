from django.core.management.base import BaseCommand
from dz2app.models import Order, Customer


class Command(BaseCommand):
    help = "Read orders customer."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        orders = Order.objects.filter(customer=customer).all()
        if orders:
            for order in orders:
                pk = order.pk
                self.stdout.write(f'Order id #{pk} is:\n{order}')
        else:
            self.stdout.write(f'Customer #{pk} is not orders')

