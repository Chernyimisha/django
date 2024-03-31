from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Customer


class Command(BaseCommand):
    help = "Create fake customer."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count fake customers')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            name = f'customer{i}'
            email = f'mail{i}@mail.com'
            phone = '12345678' + str(i)
            address = f'address{i}'
            customer = Customer(name=name, email=email, phone=phone, address=address)
            customer.save()
            self.stdout.write(f'{customer}')

