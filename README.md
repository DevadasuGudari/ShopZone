# ShopZone - Django Online Shopping Website

A multi-category e-commerce site (dairy, mobiles, groceries, electronics, fashion,
home & kitchen, books) built with Django and Bootstrap 5.

## Features
- Categories and sub-categories, product catalogue with images, brand, MRP/discount
- Flexible product specifications (RAM/Storage for phones, Shelf life for dairy, ...)
- Search, price filter, sorting, pagination
- Session-based shopping cart (add, update quantity, remove, stock limits)
- Home page with banner carousel, About page
- User sign up, login, logout, icon-only profile menu (update details, change password, orders, logout)
- Checkout (COD / UPI / Card - simulated), automatic stock reduction
- Order history and order details
- Product reviews and ratings
- Home page with banner carousel, About page
- Profile icon menu: update details, change password, my orders, logout
- Django admin for products, categories and order status management

## Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux

pip install -r requirements.txt
python manage.py makemigrations store orders
python manage.py migrate
python manage.py seed_data          # loads sample products
python manage.py createsuperuser    # for /admin
python manage.py runserver
```
Open http://127.0.0.1:8000/  and the admin at http://127.0.0.1:8000/admin/

## Project structure
```
config/     settings, root urls
store/      Category, Product, ProductAttribute, Review, listing/detail views, seed command
cart/       session cart logic and views
orders/     Order, OrderItem, checkout, order history
accounts/   signup / login / logout
templates/  HTML templates (Bootstrap 5 via CDN)
static/     CSS
```

## Adding product images
Log in to /admin, open a product and upload an image. Without an image the site
shows the category emoji as a placeholder.

## Before deploying
Set DEBUG = False, change SECRET_KEY, set ALLOWED_HOSTS, switch to PostgreSQL,
and serve static files with WhiteNoise or Nginx. Integrate Razorpay for real payments.
