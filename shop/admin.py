from django.contrib import admin
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
from django.db.models import Count

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
    list_display = ['product', 'inventory', 'product_collection', 'delivery_cost', ]
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
    list_display = ['placed_at', 'customer', 'show_cart_items_of_this_cart']
    list_per_page = number_of_items_per_page

    @admin.display(description='Cart Items')
    def show_cart_items_of_this_cart(self, cart):
        url = (
            reverse('admin:shop_cartitem_changelist') + '?' +
            urlencode({
                'cart__id': str(cart.pk)
            }))
        return format_html("<a href='{}'>{}<a/>", url, cart.cart_items_count)

    def get_queryset(self, request) :
        return super().get_queryset(request).annotate(
            cart_items_count = Count('cartitem')
        )

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'product']
    list_per_page = number_of_items_per_page

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    list_per_page = number_of_items_per_page
