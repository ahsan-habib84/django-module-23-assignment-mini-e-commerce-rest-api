from django.contrib import admin

from .models import Category, Order, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "price", "stock", "created_date"]
    list_filter = ["category"]
    search_fields = ["name", "description"]
    ordering = ["-created_date"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity", "total_price", "order_date"]
    list_filter = ["order_date"]
    search_fields = ["user__username", "product__name"]
    readonly_fields = ["total_price", "order_date"]
