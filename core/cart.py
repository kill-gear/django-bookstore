import copy

from .models import Book


class Cart:
    def __init__(self, request):
        self.session = request.session
        # cart = self.session.get(settings.BOOK_SESSION_ID)
        if x := self.session.get('CART'):
            self.cart = x
        else:
            self.cart = self.session['CART'] = {}

    # ToDo: add/remove variable quantity
    def add(self, product):

        # product.isbn should be a string
        if (id := str(product.isbn)) in self.cart:
            self.cart[id]['quantity'] += 1
        else:
            self.cart[id] = {'quantity': 1, 'price': product.price}

        self.save()

    def save(self):
        self.session.modified = True

    def subtract(self, product):
        if str(product.isbn) in self.cart:
            # x = self.cart[product.isbn]
            # quantity = x['quantity']
            id = str(product.isbn)
            if (quantity := self.cart[id]['quantity']) <= 1:
                del self.cart[id]
            else:
                self.cart[id]['quantity'] -= 1

            self.save()

    def __iter__(self):
        product_id_list = self.cart.keys()
        qs = Book.objects.filter(isbn__in=product_id_list)
        cart = copy.deepcopy(self.cart)

        # add respective book object in cart items(books)
        for book in qs:
            cart[str(book.isbn)]['object'] = book

        for item in cart.values():
            item['price'] = item['object'].price
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['CART']
