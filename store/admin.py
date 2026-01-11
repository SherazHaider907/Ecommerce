from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'created_date')
    list_filter = ('is_available', 'category')
    search_fields = ('product_name', 'description')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
