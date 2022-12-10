from django.contrib import admin

from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_per_page = 15

@admin.register(Collection) 
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ShopCollection)
class ShopCollectionAdmin(admin.ModelAdmin):
    list_display = ['collection', 'shop']
    list_per_page = 15

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'last_update']
    list_per_page = 15

@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'inventory', 'product_collection', 'delivery_cost', 'shop']
    list_per_page = 15


