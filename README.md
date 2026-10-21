# SewStylish - Custom Fashion E-commerce Platform
Cape Town, South Africa - Final Year Project by Sisipho Angel Ndzube

## Live Demo Evidence
This terminal log shows all routes working with 200 OK:
- Home, Category filter, Product detail, Cart, My Orders, Admin Dashboard
- Media file IMG_7671.jpeg served correctly

## How to Run
pip install django pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open http://127.0.0.1:8000/

## Test Flow for Video
1. / -> Home with products
2. /?category=3 -> Filter
3. /product/1/ -> Detail + Add to Cart
4. /cart/ -> View cart
5. /checkout/ -> Place order (mock payment)
6. /my-orders/ -> Track status
7. /admin-dashboard/ -> Admin updates to Sewing/Ready/Delivered

## Tech
Django 5, Bootstrap 5, SQLite, Session Cart, Auth
Models: Category, Product, Order, OrderItem
