from django.db import models
from django.utils import timezone


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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.date_ordered} {self.total_price} {self.customer} {self.products}'


