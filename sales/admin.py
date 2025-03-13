from django.contrib import admin
from .models import Sale, SaleItem, Purchase, Refund, Exchange

# Register your models here
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Purchase)
admin.site.register(Refund)
admin.site.register(Exchange)