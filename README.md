# 🛒 ShopZone — Django Online Shopping Website

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</p>

<p align="center">
  <strong>A full-stack Django e-commerce platform built to simulate a real-world online shopping experience.</strong>
</p>

<p align="center">
  🥛 Dairy &nbsp;•&nbsp;
  📱 Mobiles &nbsp;•&nbsp;
  🛒 Groceries &nbsp;•&nbsp;
  💻 Electronics &nbsp;•&nbsp;
  👕 Fashion &nbsp;•&nbsp;
  🏠 Home & Kitchen &nbsp;•&nbsp;
  📚 Books
</p>

---

## 🛍️ About ShopZone

**ShopZone** is a full-stack, multi-category **Online Shopping Website** developed using the **Django framework** and **Bootstrap 5**.

The project provides a simple and user-friendly shopping experience where users can:

- 🔎 Browse and search products
- 🏷️ Filter and sort products
- 📦 View product details
- ⭐ Read and submit reviews
- 🛒 Add products to a shopping cart
- 🔢 Update product quantities
- 💳 Proceed through checkout
- 📋 View order history
- 👤 Manage their account

The project demonstrates how **Python, Django, HTML, CSS, JavaScript, Bootstrap, and database management** can be combined to build a dynamic web application.

---

## 🎯 Project Highlights

| Feature | Description |
|---|---|
| 👤 Authentication | Signup, Login & Logout |
| 🛍️ Product Catalogue | Multi-category product browsing |
| 🔎 Search | Search products easily |
| 💰 Filtering | Price filtering and sorting |
| ⭐ Reviews | Product ratings and reviews |
| 🛒 Cart | Session-based shopping cart |
| 📦 Orders | Checkout and order management |
| 🔐 Security | Django authentication & protected pages |
| ⚙️ Admin | Manage products, users and orders |
| 📱 Responsive | Bootstrap-based responsive interface |

---

# ✨ Features

## 👤 User Features

- User sign up, login, and logout using Django authentication
- Icon-only profile menu
  - Update details
  - Change password
  - My orders
  - Logout
- Home page with banner carousel
- About page
- Browse products
- Product search
- Price filtering
- Product sorting
- Pagination
- Product details
- Product ratings and reviews
- Order history
- Order details
- Responsive user interface

---

## 🛍️ Product Features

- Product categories and sub-categories
- Product catalogue
- Product images
- Product brands
- MRP and discounts
- Product availability
- Product name and description
- Flexible product specifications

### Example Specifications

```text
📱 Mobile
RAM / Storage

🥛 Dairy
Shelf Life

💻 Electronics
Specifications

👕 Fashion
Size / Brand
````

* Product management through Django Admin

---

## 🛒 Shopping Cart

ShopZone includes a **session-based shopping cart**.

Users can:

* ➕ Add products
* 🔢 Update quantities
* 🚫 Prevent quantities beyond available stock
* ❌ Remove products
* 💰 Calculate cart totals
* 🛍️ Continue shopping
* 📦 Proceed to checkout

---

## 📦 Order Management

The ordering system supports:

* Checkout
* Cash on Delivery (COD)
* UPI simulation
* Card payment simulation
* Order creation from cart items
* Customer information storage
* Ordered product storage
* Automatic order total calculation
* Automatic stock reduction
* Order tracking
* Order status management

> 💡 Payment methods are simulated for educational purposes.

---

# 🔐 Authentication

ShopZone uses **Django's built-in authentication system** to manage:

* User registration
* Login
* Logout
* Sessions
* Protected pages
* User account management

Django authentication provides a secure foundation for managing user accounts and sessions.

---

# ⚙️ Admin Panel

Django Admin provides an easy-to-use management interface.

Administrators can manage:

* 📦 Products
* 🗂️ Categories
* 👤 Users
* 📋 Orders
* 🚚 Order status
* 🧑 Customers
* ⭐ Product reviews
* 🗃️ Other application data

The admin panel makes it easier to manage the application's database without creating separate management pages.

---

# 🛠️ Technologies Used

## 🎨 Frontend

<p>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap 5">
</p>

## ⚙️ Backend

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
</p>

## 🗄️ Database

<p>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

## 🔧 Tools

<p>
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</p>

* Python Virtual Environment

---

# 🏗️ Project Architecture

ShopZone follows Django's **Model-View-Template (MVT)** architecture.

```text
                    👤 USER
                      │
                      ▼
                🌐 URL ROUTING
                      │
                      ▼
                  ⚙️ VIEWS
                 /        \
                /          \
               ▼            ▼
          🗄️ MODELS      📄 TEMPLATES
               │              │
               ▼              ▼
          💾 DATABASE     🌐 HTML RESPONSE
                              │
                              ▼
                            👤 USER
```

## 🗄️ Models

Models define the structure of the application's database.

They are responsible for storing and retrieving application data.

## ⚙️ Views

Views contain the application's business logic.

They receive user requests, process the required operations, and return responses.

## 📄 Templates

Templates display dynamic data using HTML.

Bootstrap 5 is used to create a responsive and user-friendly interface.

Django provides database models, URL routing, views, templates, forms, authentication, sessions, and static-file functionality as core parts of the framework.

---

# 📂 Project Structure

```text
ShopZone/
│
├── config/
│   ├── settings
│   └── root urls
│
├── store/
│   ├── Category
│   ├── Product
│   ├── ProductAttribute
│   ├── Review
│   ├── Listing Views
│   ├── Detail Views
│   └── Seed Command
│
├── cart/
│   ├── Session Cart Logic
│   └── Cart Views
│
├── orders/
│   ├── Order
│   ├── OrderItem
│   ├── Checkout
│   └── Order History
│
├── accounts/
│   ├── Signup
│   ├── Login
│   └── Logout
│
├── templates/
│   └── HTML Templates
│
├── static/
│   └── CSS
│
├── requirements.txt
└── manage.py
```

---

# 🚀 Installation & Setup

Follow the steps below to run ShopZone locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/online-shopping.git
```

## 2️⃣ Navigate to the Project

```bash
cd online-shopping
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django
```

## 6️⃣ Apply Database Migrations

```bash
python manage.py makemigrations store orders
python manage.py migrate
```

## 7️⃣ Load Sample Products

```bash
python manage.py seed_data
```

## 8️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the terminal instructions to create your admin account.

## 9️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Django's official documentation provides the standard workflow for installation, creating applications, models, views, templates, forms, testing, static files, and admin customization.

---

# 🔑 Admin Panel

After creating a superuser, open:

```text
http://127.0.0.1:8000/admin/
```

The admin panel can be used to manage:

* 📦 Products
* 🗂️ Categories
* 👤 Users
* 📋 Orders
* 🚚 Order status
* 🧑 Customers

---

# 🖼️ Adding Product Images

Product images can be managed through the Django Admin Panel.

### Steps

```text
Login to /admin
      ↓
Open Products
      ↓
Select a Product
      ↓
Upload Product Image
      ↓
Save
```

If a product does not have an image, the website displays the **category emoji as a placeholder**.

---

# 🛒 Example Shopping Flow

```text
🏠 Home Page
      ↓
🛍️ Browse Products
      ↓
🔎 Search / Filter
      ↓
📦 Select Product
      ↓
📄 View Product Details
      ↓
🛒 Add to Cart
      ↓
🛍️ View Cart
      ↓
🔢 Update Quantity
      ↓
💳 Checkout
      ↓
📦 Place Order
      ↓
✅ Order Confirmation
      ↓
📋 View Order History
```

---

# 🎯 Project Objectives

The main objectives of ShopZone are:

* Understand Django web development
* Build a real-world e-commerce application
* Understand Django's MVT architecture
* Work with Django models and databases
* Implement user authentication
* Create dynamic web pages using Django templates
* Understand CRUD operations
* Implement shopping cart functionality
* Manage application data using Django Admin
* Understand session-based functionality
* Implement order management
* Gain practical experience with backend development

---

# 💡 What This Project Demonstrates

This project demonstrates practical knowledge of:

```text
Python
   ↓
Django
   ↓
MVT Architecture
   ↓
Database Models
   ↓
Authentication
   ↓
Sessions
   ↓
Shopping Cart
   ↓
Orders
   ↓
Django Admin
   ↓
Responsive UI
```

It brings multiple backend and frontend concepts together into one practical application.

---

# 🔮 Future Enhancements

The project can be extended with:

* ❤️ Wishlist functionality
* 💳 Real online payment gateway
* 💰 Razorpay integration for real payments
* 📧 Email notifications
* 🎟️ Coupon and discount system
* 🔌 REST API using Django REST Framework
* 🐘 PostgreSQL database
* ☁️ Cloud deployment
* 🔐 Improved security
* ⚡ Performance optimization
* 📱 Progressive Web App features

---

# 🌐 Before Deploying

Before deploying the project to production:

* Set `DEBUG = False`
* Change `SECRET_KEY`
* Configure `ALLOWED_HOSTS`
* Switch to PostgreSQL
* Configure production database settings
* Serve static files using WhiteNoise or Nginx
* Configure media files
* Integrate Razorpay for real payments
* Review security settings

---

# 🧪 Testing

Run Django's test suite using:

```bash
python manage.py test
```

Testing can be expanded to cover:

* User registration
* Login / Logout
* Product operations
* Search and filtering
* Cart operations
* Order creation
* Authentication
* Form validation
* Stock management
* Admin functionality

---

# 📚 Learning Resources

* [Django Official Website](https://www.djangoproject.com/?utm_source=chatgpt.com)
* [Django Documentation](https://docs.djangoproject.com/en/6.0/?utm_source=chatgpt.com)

---

# 👨‍💻 Author

## Devadasu Gudari

**B.Tech Computer Science & Engineering Graduate**

🎯 **Aspiring Full Stack Developer**

I enjoy building practical web applications, learning new technologies, solving problems, and improving my development skills through real-world projects.

### 💻 Skills Used

<p>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</p>

---

# 📄 License

This project is created for **educational and portfolio purposes**.

You are free to modify and improve the project for learning and personal development.

---

<p align="center">

## ⭐ If you found this project useful, consider giving the repository a star!

### 🛒 ShopZone — Learn • Build • Improve • Grow 🚀

</p>
