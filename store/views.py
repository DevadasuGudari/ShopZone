from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Category, Product, Review


def home(request):
    featured = Product.objects.filter(is_active=True, is_featured=True)[:8]
    latest = Product.objects.filter(is_active=True)[:8]
    return render(request, "store/home.html", {"featured": featured, "latest": latest})


def about(request):
    return render(request, "store/about.html")


def about(request):
    return render(request, "store/about.html", {"categories": Category.objects.filter(parent__isnull=True)})


def product_list(request, category_slug=None):
    products = Product.objects.filter(is_active=True).select_related("category")
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ids = [category.id] + list(category.children.values_list("id", flat=True))
        products = products.filter(category_id__in=ids)

    q = request.GET.get("q", "").strip()
    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(brand__icontains=q) | Q(description__icontains=q)
        )

    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    if min_price and min_price.isdigit():
        products = products.filter(price__gte=min_price)
    if max_price and max_price.isdigit():
        products = products.filter(price__lte=max_price)

    sort = request.GET.get("sort", "new")
    ordering = {
        "new": "-created",
        "price_low": "price",
        "price_high": "-price",
        "name": "name",
    }.get(sort, "-created")
    products = products.order_by(ordering)

    page = Paginator(products, 12).get_page(request.GET.get("page"))
    params = request.GET.copy()
    params.pop("page", None)

    return render(
        request,
        "store/product_list.html",
        {
            "category": category,
            "page": page,
            "q": q,
            "sort": sort,
            "min_price": min_price or "",
            "max_price": max_price or "",
            "querystring": params.urlencode(),
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(category=product.category, is_active=True).exclude(
        pk=product.pk
    )[:4]
    return render(
        request,
        "store/product_detail.html",
        {
            "product": product,
            "related": related,
            "reviews": product.reviews.select_related("user"),
        },
    )


@login_required
@require_POST
def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)
    try:
        rating = int(request.POST.get("rating", 5))
    except ValueError:
        rating = 5
    rating = min(max(rating, 1), 5)
    Review.objects.update_or_create(
        product=product,
        user=request.user,
        defaults={"rating": rating, "comment": request.POST.get("comment", "").strip()},
    )
    messages.success(request, "Thanks for your review!")
    return redirect(product.get_absolute_url())
