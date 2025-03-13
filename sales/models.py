from django.db import models
from inventory.models import Product  # Import the Product model

class Sale(models.Model):
    # Define your model fields here
    pass

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='sale_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} at {self.price}"

class Purchase(models.Model):
    # Define your model fields here
    pass

class Refund(models.Model):
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund for reason: {self.reason}"

class Exchange(models.Model):
    sale = models.ForeignKey(Sale, related_name='exchanges', on_delete=models.CASCADE)
    old_product = models.ForeignKey(Product, related_name='old_exchanges', on_delete=models.CASCADE)
    new_product = models.ForeignKey(Product, related_name='new_exchanges', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)