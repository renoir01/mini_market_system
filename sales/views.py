from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Sale, SaleItem, Purchase, Refund, Exchange
from .forms import SaleForm, SaleItemForm, RefundForm, ExchangeForm
from django.http import HttpResponse

def is_cashier(user):
    return user.role == 'cashier'

def is_owner(user):
    return user.role == 'owner'

@login_required
@user_passes_test(is_cashier)
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})

@login_required
@user_passes_test(is_cashier)
def sale_detail(request, pk):
    sale = Sale.objects.get(pk=pk)
    sale_items = SaleItem.objects.filter(sale=sale)
    return render(request, 'sales/sale_detail.html', {'sale': sale, 'sale_items': sale_items})

@login_required
@user_passes_test(is_cashier)
def process_sale(request):
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        sale_item_form = SaleItemForm(request.POST)
        if sale_form.is_valid() and sale_item_form.is_valid():
            sale = sale_form.save()
            sale_item = sale_item_form.save(commit=False)
            sale_item.sale = sale
            sale_item.save()
            return redirect('sales:sale-list')
    else:
        sale_form = SaleForm()
        sale_item_form = SaleItemForm()
    return render(request, 'sales/process_sale.html', {'sale_form': sale_form, 'sale_item_form': sale_item_form})

@login_required
@user_passes_test(is_owner)
def view_profit(request):
    profit = Purchase.calculate_profit()
    return render(request, 'sales/view_profit.html', {'profit': profit})

@login_required
@user_passes_test(is_owner)
def generate_monthly_report(request):
    # Report generation logic here
    return HttpResponse("Report generated")

@login_required
@user_passes_test(is_cashier)
def process_refund(request):
    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:sale-list')
    else:
        form = RefundForm()
    return render(request, 'sales/process_refund.html', {'form': form})

@login_required
@user_passes_test(is_cashier)
def process_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:sale-list')
    else:
        form = ExchangeForm()
    return render(request, 'sales/process_exchange.html', {'form': form})

@login_required
@user_passes_test(is_owner)
def purchase_history(request):
    purchases = Purchase.objects.all()
    return render(request, 'sales/purchase_history.html', {'purchases': purchases})