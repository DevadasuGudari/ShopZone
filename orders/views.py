from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from cart.cart import Cart

from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = Cart(request)
    items = list(cart)
    if not items:
        messages.info(request, "Your cart is empty.")
        return redirect("store:product_list")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # re-check stock with row locks where the database supports it
                for item in items:
                    product = item["product"].__class__.objects.select_for_update().get(
                        pk=item["product"].pk
                    )
                    if product.stock < item["quantity"]:
                        messages.error(
                            request, f"Only {product.stock} left of {product.name}. Please update your cart."
                        )
                        return redirect("cart:detail")

                order = form.save(commit=False)
                order.user = request.user
                order.total = cart.get_total_price()
                order.status = "confirmed"
                order.save()

                for item in items:
                    product = item["product"]
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_name=product.name,
                        price=item["price"],
                        quantity=item["quantity"],
                    )
                    product.stock -= item["quantity"]
                    product.save(update_fields=["stock"])

            cart.clear()
            return redirect("orders:success", order_id=order.id)
    else:
        user = request.user
        form = CheckoutForm(
            initial={
                "full_name": user.get_full_name() or user.username,
                "email": user.email,
            }
        )

    return render(
        request,
        "orders/checkout.html",
        {"form": form, "items": items, "total": cart.get_total_price()},
    )


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/success.html", {"order": order})


@login_required
def my_orders(request):
    return render(request, "orders/my_orders.html", {"orders": request.user.orders.all()})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/detail.html", {"order": order})
