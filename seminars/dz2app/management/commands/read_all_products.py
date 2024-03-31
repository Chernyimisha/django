from django.core.management.base import BaseCommand
from dz2app.models import Product


class Command(BaseCommand):
    help = "Read all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            pk = product.pk
            self.stdout.write(f'product id #{pk} is: {product}')

