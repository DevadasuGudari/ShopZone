from cart.cart import Cart

from .models import Category


def shop_globals(request):
    return {
        "nav_categories": Category.objects.filter(parent__isnull=True),
        "cart_count": len(Cart(request)),
    }
