from django.contrib import admin
from .models import Category, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total','status','created_at']
    list_filter = ['status']
    inlines = [OrderItemInline]

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
