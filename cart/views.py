from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from store.models import Product

from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart, "items": list(cart)})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if not product.in_stock:
        messages.error(request, "Sorry, this product is out of stock.")
        return redirect(product.get_absolute_url())
    try:
        qty = int(request.POST.get("quantity", 1))
    except ValueError:
        qty = 1
    cart.add(product, quantity=qty)
    messages.success(request, f"Added {product.name} to your cart.")
    if request.POST.get("buy_now"):
        return redirect("orders:checkout")
    return redirect(request.POST.get("next") or "cart:detail")


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        qty = int(request.POST.get("quantity", 1))
    except ValueError:
        qty = 1
    cart.add(product, quantity=qty, override=True)
    return redirect("cart:detail")


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(get_object_or_404(Product, id=product_id))
    messages.info(request, "Item removed from cart.")
    return redirect("cart:detail")
