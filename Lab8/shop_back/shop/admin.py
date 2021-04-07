from django.contrib import admin
from .models import Category,Product


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name','category','price','is_active']