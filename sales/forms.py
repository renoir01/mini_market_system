from django import forms
from .models import Sale, SaleItem, Refund, Exchange

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['sale', 'product', 'quantity', 'price']

class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['sale', 'reason']

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['sale', 'old_product', 'new_product']