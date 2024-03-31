from django.utils import timezone
from django.core.management.base import BaseCommand
from dz2app.models import Product
import random


class Command(BaseCommand):
    help = "Create fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count fake products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            name = f'product{i}'
            description = f'description{i}'
            price = random.uniform(0, 1000)
            volume = 5 * price
            product = Product(name=name, description=description, price=price, volume=volume)
            product.save()
            self.stdout.write(f'{product} saved successfully')

