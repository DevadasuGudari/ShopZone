import copy
from decimal import Decimal

from store.models import Product

CART_SESSION_ID = "cart"


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override=False):
        pid = str(product.id)
        if pid not in self.cart:
            self.cart[pid] = {"quantity": 0}
        if override:
            qty = quantity
        else:
            qty = self.cart[pid]["quantity"] + quantity
        qty = min(qty, product.stock)
        if qty <= 0:
            self.remove(product)
            return
        self.cart[pid]["quantity"] = qty
        self.save()

    def remove(self, product):
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session.pop(CART_SESSION_ID, None)
        self.session.modified = True

    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart.keys())
        cart = copy.deepcopy(self.cart)
        for product in products:
            item = cart[str(product.id)]
            item["product"] = product
            item["price"] = product.price
            item["total_price"] = product.price * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum((item["total_price"] for item in self), Decimal("0"))
