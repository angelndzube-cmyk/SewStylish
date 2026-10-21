from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): 
        return self.name

class Product(models.Model):
    SIZES = [('S','S'),('M','M'),('L','L'),('XL','XL'),('Free','Free Size')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZES, default='M')
    stock = models.IntegerField(default=10)
    image = models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.title

class Order(models.Model):
    STATUS = [('Pending','Pending'),('Paid','Paid'),('Sewing','Sewing'),('Ready','Ready'),('Delivered','Delivered')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=255, default='')
    def __str__(self): 
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
