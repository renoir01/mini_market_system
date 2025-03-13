from django import forms
from .models import Refund, Exchange

class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['sale', 'reason']

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['sale', 'old_product', 'new_product']