from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Customer


class Command(BaseCommand):
    help = "Update customer."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('name', type=str, help='name customers')
        parser.add_argument('email', type=str, help='email customers')
        parser.add_argument('phone', type=str, help='phone customers')
        parser.add_argument('address', type=str, help='address customers')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        if customer is not None:
            customer.name = kwargs['name']
            customer.email = kwargs['email']
            customer.phone = kwargs['phone']
            customer.address = kwargs['address']
            customer.save()
            self.stdout.write(f'customer id #{pk} updated.\nNew value: {customer}')
        else:
            self.stdout.write(f'customer id #{pk} is not defined')


