from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')
    search_fields = ('name',)
    ordering = ('name',)
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Product count'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'is_active', 'category')
    list_filter = ('is_active', 'category', 'price')
    search_fields = ('name', 'description')
    list_editable = ('price', 'count', 'is_active')
    ordering = ('-price',)
    list_per_page = 20