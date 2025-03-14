from django.contrib import admin
from django.urls import path, include
from inventory.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
    path('users/', include('users.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include('api.urls')),  # Add this line to include api.urls
    path('', include('django.contrib.auth.urls')),  # For login, logout, password management
]