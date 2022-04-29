from django.contrib import admin
from core.models import Category, SubCategory, Book, Customer, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

