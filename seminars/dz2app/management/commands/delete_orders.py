from django.core.management.base import BaseCommand
from dz2app.models import Order


class Command(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('diap', type=str, help='Order ID')

    def handle(self, *args, **kwargs):
        diap = kwargs.get('diap').split('-')
        for i in range(int(diap[0]), int(diap[1]) + 1):
            order = Order.objects.filter(pk=i).first()
            if order is not None:
                order.delete()
                self.stdout.write(f'{order} deleted')

