from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Главная страница со списком категорий
    path('', views.category_list, name='category_list'),

    # Детали категории
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),

    # Список товаров в категории
    path('category/<int:category_id>/products/', views.product_list, name='product_list'),

    # Детали товара
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Добавление товара в корзину
    path('cart/add/', views.add_to_cart, name='add_to_cart'),

    # Корзина
    path('cart/', views.order_detail, name='order_detail'),

    # История заказов
    path('orders/', views.order_history, name='order_history'),

    # Страница поддержки
    path('support/', views.support_page, name='support'),  # Your support page
    path('support/message/', views.support_message, name='support_message')

]
