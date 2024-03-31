from django.core.management.base import BaseCommand
from dz2app.models import Customer


class Command(BaseCommand):
    help = "Read all customer."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        for customer in customers:
            pk = customer.pk
            self.stdout.write(f'customer id #{pk} is: {customer}')

