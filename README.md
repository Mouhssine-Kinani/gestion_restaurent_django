🏪 Restaurant Manager Enhanced

A Django-based Restaurant Management System for managing menu items, orders, and tables, with user authentication and an admin dashboard for clear insights.

📌 Features

User Authentication: Register, Login, and Logout.

Admin Panel: Manage all menu items, orders, and tables from Django admin.

Menu Management: Add, update, delete, and view menu items.

Order Management: Create, update, delete, and view orders.

Tables Management: Assign orders to tables.

Search & Filter: Quickly find orders or menu items using search queries.

Sorting: Lists sorted alphabetically or by other criteria.

Dashboard: Overview of orders, menu items, and table occupancy.

Secure Access: All management actions require login.

Responsive Design Ready: Can be enhanced with CSS frameworks.

💻 Tech Stack

Backend: Django 5.x

Database: SQLite (default, can switch to PostgreSQL/MySQL)

Frontend: HTML, Django Templates

Authentication: Django built-in auth system

Version Control: Git & GitHub

🏗️ Project Structure
restaurant_manager/
│
├── restaurant_manager/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/               # App
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/restaurant/ # HTML templates
│
├── db.sqlite3
└── manage.py

🚀 Getting Started
1. Clone the repository
git clone https://github.com/banumariwan/restaurant-manager-enhanced.git
cd restaurant-manager-enhanced

2. Install dependencies
pip install django

3. Apply migrations
python manage.py migrate

4. Create a superuser (Admin)
python manage.py createsuperuser


Follow prompts to set username, email, and password.

5. Run the server
python manage.py runserver


Visit http://127.0.0.1:8000
 in your browser.

🎨 Templates Included

register_user.html

login_user.html

menu_list.html

order_list.html

add/update/delete templates for menu and orders

All templates are unstyled by default and ready for CSS/JS enhancements.

🔍 Dashboard

Dashboard displays:

Total orders

Active tables

Most popular menu items

Orders by status

Search and sort functionality included.
