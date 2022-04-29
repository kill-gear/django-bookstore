import re
from .models import Book
from .cart import Cart


def cart_renderer(request):
    return {'cart':list(Cart(request))}