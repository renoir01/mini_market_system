from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Product

@receiver(post_save, sender=Product)
def notify_low_stock(sender, instance, **kwargs):
    if instance.stock_level < 5:
        send_mail(
            'Low Stock Alert',
            f'The product {instance.name} is running low on stock.',
            'admin@minimarket.com',
            ['owner@minimarket.com'],
        )