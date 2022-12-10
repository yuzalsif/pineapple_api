from django.contrib import admin

from .models import *


number_of_items_per_page: int = 15
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_per_page = number_of_items_per_page

@admin.register(Collection) 
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ShopCollection)
class ShopCollectionAdmin(admin.ModelAdmin):
    list_display = ['collection', 'shop']
    list_per_page = number_of_items_per_page

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'last_update']
    list_per_page = number_of_items_per_page

@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'inventory', 'product_collection', 'delivery_cost', 'shop']
    list_per_page = number_of_items_per_page

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer', 'shop']
    list_per_page = number_of_items_per_page

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'unit_price']
    list_per_page = number_of_items_per_page

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'customer']
    list_per_page = number_of_items_per_page

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'product']
    list_per_page = number_of_items_per_page
