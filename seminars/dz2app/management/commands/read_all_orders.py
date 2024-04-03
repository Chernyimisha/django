from django.core.management.base import BaseCommand
from dz2app.models import Order


class Command(BaseCommand):
    help = "Read all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            pk = order.pk
            self.stdout.write(f'Order id #{pk} is:\n{order}')

