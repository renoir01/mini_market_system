import csv
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from sales.models import Sale, SaleItem, Purchase

class Command(BaseCommand):
    help = 'Generate a monthly sales report'

    def handle(self, *args, **kwargs):
        current_month = now().month
        current_year = now().year

        sales = Sale.objects.filter(date__year=current_year, date__month=current_month)
        purchases = Purchase.objects.filter(date__year=current_year, date__month=current_month)
        total_sales = sum(sale.total_amount for sale in sales)
        total_purchases = sum(purchase.price * purchase.quantity for purchase in purchases)
        profit = total_sales - total_purchases

        report_filename = f'monthly_report_{current_year}_{current_month}.csv'
        with open(report_filename, 'w', newline='') as csvfile:
            fieldnames = ['Date', 'Total Sales', 'Total Purchases', 'Profit']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'Date': f'{current_year}-{current_month}',
                'Total Sales': total_sales,
                'Total Purchases': total_purchases,
                'Profit': profit
            })

        self.stdout.write(self.style.SUCCESS(f'Monthly report generated: {report_filename}'))