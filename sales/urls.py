from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('sales/', views.sale_list, name='sale-list'),
    path('sales/<int:pk>/', views.sale_detail, name='sale-detail'),
    path('sales/process/', views.process_sale, name='process-sale'),
    path('profit/', views.view_profit, name='view-profit'),
    path('generate-report/', views.generate_monthly_report, name='generate-report'),
    path('refund/', views.process_refund, name='process-refund'),
    path('exchange/', views.process_exchange, name='process-exchange'),
    path('purchase-history/', views.purchase_history, name='purchase-history'),
]