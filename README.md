# SewStylish 👗 - Custom Fashion E-commerce Platform
Custom-made dresses, alterations and fashion design - Cape Town, South Africa

## Overview
SewStylish is a Django-based e-commerce platform for a local fashion boutique.
Customers can browse collections, add to cart, checkout with delivery details and track orders.
Business owner manages products and orders via admin dashboard.

## Live Demo
Server runs at http://127.0.0.1:8000/ - All routes tested 200 OK
- Home with category filter & search
- Product detail
- Session-based cart
- Checkout (mock payment)
- My Orders tracking
- Admin Dashboard for order status updates

## Features
- Browse, Search, Filter by Category (Dresses, Alterations, Custom Design)
- Product Detail with Size / Stock / Image (Pillow)
- Cart with quantity & total calculation
- Checkout with phone + address
- Order status flow: Pending -> Paid -> Sewing -> Ready -> Delivered
- Authentication: Signup, Login, Logout
- Admin: Django Admin + Custom Admin Dashboard

## Tech Stack
Python 3.12, Django 5, Bootstrap 5, SQLite, Django Auth, Pillow

## Models
Category, Product, Order, OrderItem, User (built-in)

## How to Run Locally
pip install django pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open http://127.0.0.1:8000/

## Project Structure
sewstylish_project/settings.py - media config & context processor
shop/models.py - 4 models
shop/views.py - 10 views
templates/shop/ - 6 templates
