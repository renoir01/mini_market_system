from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'price', 'stock_level', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')