from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from store.models import Category, Product, ProductAttribute

DATA = {
    ("Dairy", "🥛"): [
        ("Fresh Full Cream Milk 1L", "Amul", 68, 72, 80, {"Fat": "6%", "Shelf life": "2 days", "Pack": "1 L"}),
        ("Paneer 200g", "Mother Dairy", 90, 100, 40, {"Weight": "200 g", "Shelf life": "7 days"}),
        ("Salted Butter 500g", "Amul", 285, 300, 50, {"Weight": "500 g", "Shelf life": "6 months"}),
        ("Set Curd 400g", "Nandini", 40, 45, 60, {"Weight": "400 g", "Shelf life": "5 days"}),
        ("Cheese Slices 200g", "Britannia", 150, 165, 35, {"Slices": "10", "Shelf life": "8 months"}),
    ],
    ("Mobiles", "📱"): [
        ("Galaxy M35 5G (8GB/128GB)", "Samsung", 18999, 24999, 25, {"RAM": "8 GB", "Storage": "128 GB", "Battery": "6000 mAh", "Display": "6.6 inch AMOLED"}),
        ("Redmi Note 13 Pro (8GB/256GB)", "Xiaomi", 23999, 28999, 30, {"RAM": "8 GB", "Storage": "256 GB", "Camera": "200 MP", "Battery": "5100 mAh"}),
        ("iPhone 15 (128GB)", "Apple", 69900, 79900, 12, {"Storage": "128 GB", "Chip": "A16 Bionic", "Camera": "48 MP"}),
        ("Realme Narzo 70 (6GB/128GB)", "Realme", 13999, 16999, 40, {"RAM": "6 GB", "Storage": "128 GB", "Battery": "5000 mAh"}),
    ],
    ("Groceries", "🛒"): [
        ("Basmati Rice 5kg", "India Gate", 649, 780, 70, {"Weight": "5 kg", "Type": "Long grain"}),
        ("Sunflower Oil 1L", "Fortune", 135, 150, 90, {"Volume": "1 L"}),
        ("Toor Dal 1kg", "Tata Sampann", 165, 185, 60, {"Weight": "1 kg"}),
        ("Tea Powder 500g", "Red Label", 245, 270, 55, {"Weight": "500 g"}),
    ],
    ("Electronics", "💻"): [
        ("Wireless Earbuds", "boAt", 1299, 2999, 100, {"Battery": "40 hrs", "Bluetooth": "5.3"}),
        ("Smart Watch", "Noise", 2499, 4999, 45, {"Display": "1.85 inch", "Battery": "7 days"}),
        ("Power Bank 20000mAh", "Mi", 1799, 2199, 60, {"Capacity": "20000 mAh", "Ports": "3"}),
    ],
    ("Fashion", "👕"): [
        ("Men's Cotton T-Shirt", "Roadster", 399, 799, 120, {"Fabric": "Cotton", "Fit": "Regular"}),
        ("Women's Kurti", "Biba", 899, 1599, 70, {"Fabric": "Rayon", "Sleeve": "3/4"}),
        ("Running Shoes", "Puma", 2499, 4499, 50, {"Type": "Running", "Sole": "EVA"}),
    ],
    ("Home & Kitchen", "🏠"): [
        ("Non-stick Cookware Set (3 pc)", "Prestige", 1599, 2499, 35, {"Pieces": "3", "Material": "Aluminium"}),
        ("Mixer Grinder 750W", "Bajaj", 2799, 3999, 28, {"Power": "750 W", "Jars": "3"}),
    ],
    ("Books", "📚"): [
        ("Atomic Habits", "James Clear", 399, 599, 80, {"Pages": "320", "Language": "English"}),
        ("Python Crash Course", "Eric Matthes", 649, 899, 40, {"Pages": "552", "Language": "English"}),
    ],
}


class Command(BaseCommand):
    help = "Load sample categories and products"

    def handle(self, *args, **options):
        count = 0
        for (cat_name, icon), items in DATA.items():
            category, _ = Category.objects.get_or_create(
                slug=slugify(cat_name), defaults={"name": cat_name, "icon": icon}
            )
            for i, (name, brand, price, mrp, stock, attrs) in enumerate(items):
                product, created = Product.objects.get_or_create(
                    slug=slugify(name),
                    defaults={
                        "category": category,
                        "name": name,
                        "brand": brand,
                        "price": Decimal(price),
                        "mrp": Decimal(mrp),
                        "stock": stock,
                        "is_featured": i == 0,
                        "description": f"{name} by {brand}. Genuine product with fast delivery.",
                    },
                )
                if created:
                    count += 1
                    for k, v in attrs.items():
                        ProductAttribute.objects.create(product=product, name=k, value=v)
        self.stdout.write(self.style.SUCCESS(f"Seed complete. {count} new products added."))
