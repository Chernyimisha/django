from django.db import models
from django.utils import timezone
import json


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}, {self.address}, {self.registration_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} {self.price} {self.volume} {self.description}'


class Order(models.Model):

    id_product_QUANTITY: dict = {}

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, unique=False)
    date_ordered = models.DateTimeField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    view_products = models.TextField(max_length=1000, blank=True)

    def get_product(self):
        result = ''
        products = self.products.all()
        view_products = json.loads(self.view_products)
        for i, product in enumerate(products, 1):
            count = view_products[f'{product.pk}']
            product_summ = product.price * count
            result += f'{i}. {product.name} {count} шт. x {product.price} руб. на сумму {product_summ} руб.\n\t'
        return result

    @staticmethod
    def get_product_set_orders(set_orders):
        result = ''
        result_products = set()
        result_view_products = {}
        for order in set_orders:
            products = order.products.all()
            for product in products:
                result_products.add(product)
            view_products = json.loads(str(order.view_products))
            for key, value in view_products.items():
                if key not in result_view_products:
                    result_view_products[key] = value
                else:
                    result_view_products[key] += value

        for i, product in enumerate(result_products, 1):
            count = result_view_products[f'{product.pk}']
            product_summ = product.price * count
            result += f'{i}. {product.name} {count} шт. x {product.price} руб. на сумму {product_summ} руб.\n\t'

        return result

    def __str__(self):
        return f'Datetime order: {self.date_ordered},\nTotal: {self.total_price},\n' \
               f'Customer: {self.customer}' \
               f'\nProducts:\n\t{self.get_product()}'


