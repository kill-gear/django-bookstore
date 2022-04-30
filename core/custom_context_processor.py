import re
from .models import Book
from .cart import Cart


def cart_renderer(request):
    cart = Cart(request)
    return {'cart':list(cart), 'cart_total':cart.get_total_price()}