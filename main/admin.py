from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created_at', 'updated_at')
    list_editable = ('price', 'stock')
    ordering = ('-created_at',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at', 'updated_at')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__created_at',)
    ordering = ('-order__created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'rating')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

