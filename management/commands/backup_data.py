import json
from django.core.management.base import BaseCommand
from django.core import serializers
from inventory.models import Product, Category
from sales.models import Sale, SaleItem, Purchase
from users.models import User

class Command(BaseCommand):
    help = 'Backup data to a JSON file'

    def handle(self, *args, **kwargs):
        data = {
            'users': serializers.serialize('json', User.objects.all()),
            'products': serializers.serialize('json', Product.objects.all()),
            'categories': serializers.serialize('json', Category.objects.all()),
            'sales': serializers.serialize('json', Sale.objects.all()),
            'sale_items': serializers.serialize('json', SaleItem.objects.all()),
            'purchases': serializers.serialize('json', Purchase.objects.all()),
        }
        with open('backup.json', 'w') as f:
            f.write(json.dumps(data, indent=4))
        self.stdout.write(self.style.SUCCESS('Data backup completed successfully'))