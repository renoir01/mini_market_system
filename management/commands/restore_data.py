import json
from django.core.management.base import BaseCommand
from django.core import serializers
from inventory.models import Product, Category
from sales.models import Sale, SaleItem, Purchase
from users.models import User

class Command(BaseCommand):
    help = 'Restore data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('backup.json', 'r') as f:
            data = json.load(f)
            for model, records in data.items():
                ModelClass = serializers.deserialize('json', records)
                for record in ModelClass:
                    record.save()
        self.stdout.write(self.style.SUCCESS('Data restored successfully'))