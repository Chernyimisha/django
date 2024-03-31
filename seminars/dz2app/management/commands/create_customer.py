from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name customers')
        parser.add_argument('email', type=str, help='email customers')
        parser.add_argument('phone', type=str, help='phone customers')
        parser.add_argument('address', type=str, help='address customers')

    def handle(self, *args, **kwargs):
        customer = Customer(name=kwargs['name'], email=kwargs['email'],
                            phone=kwargs['phone'], address=kwargs['address'])
        customer.save()
        self.stdout.write(f'{customer}')

