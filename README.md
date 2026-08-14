# 🛒 Online Shopping Website

A full-stack **Online Shopping Website** developed using the **Django framework**. This project provides a simple and user-friendly e-commerce experience where users can browse products, view product details, manage their shopping cart, and place orders.

The project demonstrates the practical use of **Python, Django, HTML, CSS, JavaScript, and database management** to build a dynamic web application.

## 📌 Project Overview

The Online Shopping Website is designed to simulate a real-world e-commerce platform.

Users can explore available products, view product information, add products to their cart, update quantities, and proceed through the ordering process.

The project uses **Django's Model-View-Template (MVT) architecture**, database models, URL routing, templates, forms, authentication, and the Django Admin Panel.

Django provides built-in functionality for authentication, forms, database interaction, sessions, administration, and other common web application requirements.

## ✨ Features

### 👤 User Features

* User registration
* User login and logout
* User authentication
* Browse products
* View product details
* Search and browse products
* Add products to cart
* Update product quantity
* Remove products from cart
* View cart total
* Place orders
* View order information
* Responsive user interface

### 🛍️ Product Features

* Product listing
* Product details
* Product name and description
* Product price
* Product category
* Product availability
* Product management through Django Admin

### 🛒 Shopping Cart

* Add products to cart
* Increase or decrease quantity
* Remove products
* Calculate total price
* Maintain cart information using Django sessions/database

### 📦 Order Management

* Create orders from cart items
* Store customer information
* Store ordered products
* Calculate order totals
* Track order information

### 🔐 Authentication

The application uses Django's built-in authentication system for managing users, login sessions, and protected pages.

### ⚙️ Admin Panel

Django Admin is used to manage:

* Products
* Categories
* Users
* Orders
* Customers
* Other application data

Django includes an automatic administration interface that can be customized for application models.

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap *(if used in your project)*

### Backend

* Python
* Django

### Database

* SQLite

### Tools

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

## 🏗️ Project Architecture

The project follows Django's **Model-View-Template (MVT)** architecture.

```text
User
  │
  ▼
URL Routing
  │
  ▼
Views
  │
  ├── Models ───► Database
  │
  ▼
Templates
  │
  ▼
HTML Response
  │
  ▼
User
```

### Models

Models define the structure of the application's database and are used to store and retrieve application data.

### Views

Views contain the application logic and process user requests before returning responses.

### Templates

Templates are used to display dynamic data to users through HTML pages.

Django provides database models, URL routing, views, templates, forms, authentication, sessions, and static-file functionality as core parts of the framework.

## 📂 Project Structure

```text
online-shopping/
│
├── manage.py
│
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── db.sqlite3
│
├── requirements.txt
│
└── README.md
```

> Folder names may be different depending on your actual Django project structure.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/online-shopping.git
```

### 2. Navigate to the Project

```bash
cd online-shopping
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the terminal instructions to create your admin account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Django's official documentation provides the standard workflow for installation, creating applications, models, views, templates, forms, testing, static files, and admin customization.

## 🔑 Admin Panel

After creating a superuser, open:

```text
http://127.0.0.1:8000/admin/
```

The admin can be used to manage application data such as:

* Products
* Categories
* Users
* Orders
* Customers

## 📋 Example User Flow

```text
Home Page
    ↓
Browse Products
    ↓
Select Product
    ↓
View Product Details
    ↓
Add to Cart
    ↓
View Cart
    ↓
Update Quantity
    ↓
Checkout / Place Order
    ↓
Order Confirmation
```

## 🎯 Project Objectives

The main objectives of this project are:

* To understand Django web development.
* To build a real-world e-commerce application.
* To understand Django's MVT architecture.
* To work with Django models and databases.
* To implement user authentication.
* To create dynamic web pages using Django templates.
* To understand CRUD operations.
* To implement shopping cart functionality.
* To manage application data using Django Admin.
* To gain practical experience with backend development.

## 🔮 Future Enhancements

The project can be extended with:

* Online payment gateway
* Product reviews and ratings
* Wishlist functionality
* Order tracking
* Email notifications
* Product filtering
* Advanced product search
* User profile management
* Multiple product categories
* Coupon and discount system
* REST API using Django REST Framework
* PostgreSQL database
* Cloud deployment
* Improved security and performance

## 🧪 Testing

Run Django's test suite using:

```bash
python manage.py test
```

Testing can be expanded to cover:

* User registration
* Login/logout
* Product operations
* Cart operations
* Order creation
* Authentication
* Form validation

## 📚 Learning Resources

* [Django Official Website](https://www.djangoproject.com/?utm_source=chatgpt.com)
* [Django Documentation](https://docs.djangoproject.com/en/6.0/?utm_source=chatgpt.com)

## 👨‍💻 Author

**Devadasu Gudari**

B.Tech Computer Science & Engineering Graduate
Aspiring Full Stack Developer

### Skills Used

* HTML
* CSS
* JavaScript
* Python
* Django
* SQL
* Git & GitHub

## 📄 License

This project is created for **educational and portfolio purposes**.

You are free to modify and improve the project for learning and personal development.

---

⭐ **If you found this project useful, consider giving the repository a star!**
