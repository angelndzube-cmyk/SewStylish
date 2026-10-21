from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category, Order, OrderItem
from decimal import Decimal

def home(request):
    category_id = request.GET.get('category')
    search = request.GET.get('search')
    products = Product.objects.all().order_by('-date_added')
    if category_id:
        products = products.filter(category_id=category_id)
    if search:
        products = products.filter(title__icontains=search)
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_view')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = Decimal('0.00')
    for pid, qty in cart.items():
        try:
            p = Product.objects.get(id=pid)
            sub = p.price * qty
            total += sub
            items.append({'product': p, 'qty': qty, 'sub': sub})
        except: pass
    return render(request, 'shop/cart.html', {'items': items, 'total': total})

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('home')
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        items_data = []
        total = Decimal('0.00')
        for pid, qty in cart.items():
            p = Product.objects.get(id=pid)
            total += p.price * qty
            items_data.append((p, qty))
        order = Order.objects.create(user=request.user, total=total, phone=phone, address=address, status='Paid')
        for p, qty in items_data:
            OrderItem.objects.create(order=order, product=p, quantity=qty, price=p.price)
        request.session['cart'] = {}
        return redirect('my_orders')
    return render(request, 'shop/checkout.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/my_orders.html', {'orders': orders})

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'shop/admin_dashboard.html', {'orders': orders})

@user_passes_test(is_admin)
def update_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
    return redirect('admin_dashboard')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
