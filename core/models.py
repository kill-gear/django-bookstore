from ast import Or
from enum import unique
from itertools import product
from unicodedata import category, name
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} : {self.category}'


# TODO:
#       Separate Author model
class Book(models.Model):
    isbn = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        'SubCategory', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=300)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    about = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    pincode = models.PositiveIntegerField()
    mobile = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        indexes = [
            models.Index(fields=['pincode']),
            models.Index(fields=['mobile']),
        ]

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='OrderItem')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Order ID:{self.id} Name:{self.customer.name}'


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        unique_together = [['book', 'order']]

    def __str__(self) -> str:
        return f'Order ID:{self.order_id} || Book:{self.book_id} || Quantity:{self.quantity}'
