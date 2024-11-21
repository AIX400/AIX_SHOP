from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Product, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def category_list(request):
    """Список всех категорий"""
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {'categories': categories})

def product_list(request, category_id=None):
    """Список товаров, фильтрация по категории"""
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
    else:
        category = None
        products = Product.objects.all()

    return render(request, 'shop/product_list.html', {
        'category': category,
        'products': products
    })

def product_detail(request, product_id):
    """Детали товара"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
@require_POST
def add_to_cart(request):
    """Добавление товара в корзину"""
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id)

    # Получение или создание заказа "в ожидании" для текущего пользователя
    order, created = Order.objects.get_or_create(user=request.user, status='pending')

    # Добавление товара в заказ
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += quantity
    order_item.price = product.price
    order_item.save()

    return JsonResponse({'success': True, 'message': 'Товар добавлен в корзину!'})

@login_required
def order_detail(request):
    """Отображение текущего заказа пользователя"""
    order = Order.objects.filter(user=request.user, status='pending').first()
    return render(request, 'shop/order_detail.html', {'order': order})

@login_required
def order_history(request):
    """История заказов пользователя"""
    orders = Order.objects.filter(user=request.user).exclude(status='pending')
    return render(request, 'shop/order_history.html', {'orders': orders})

def support_page(request):
    """Страница поддержки"""
    return render(request, 'shop/support.html')  # Путь к шаблону 'support.html'.

def category_detail(request, category_id):
    """Детали категории"""
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})
# views.py
from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    """Список всех категорий и товаров"""
    categories = Category.objects.all()  # Получаем все категории
    products = Product.objects.all()  # Получаем все товары
    return render(request, 'shop/home.html', {'categories': categories, 'products': products})

from django.shortcuts import render

def support_view(request):
    return render(request, 'shop/support.html')  # Make sure the template exists

def category_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'categories': categories, 'products': products})

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def support_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Здесь сохраните данные в БД или отправьте email
        messages.success(request, 'Ваше сообщение отправлено!')
        return redirect('/')
    return render(request, 'support_form.html')