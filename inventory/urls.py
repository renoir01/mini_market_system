from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('products/add/', views.product_add, name='product-add'),
    path('products/<int:pk>/edit/', views.product_edit, name='product-edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),
    path('products/', views.product_list, name='product-list'),
    path('', views.inventory_home, name='inventory-home'),  # Add this line for inventory/
]