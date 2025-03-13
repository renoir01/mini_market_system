from django.test import TestCase
from django.urls import reverse
from .models import Sale, SaleItem
from users.models import User
from inventory.models import Product

class SaleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cashier', password='12345')
        self.product = Product.objects.create(name='Test Product', price=100, stock_level=10)
        self.sale = Sale.objects.create(total_amount=200, payment_method='cash', cashier=self.user)
        self.sale_item = SaleItem.objects.create(sale=self.sale, product=self.product, quantity=2, price=100)

    def test_sale_creation(self):
        self.assertEqual(self.sale.total_amount, 200)
        self.assertEqual(self.sale.payment_method, 'cash')
        self.assertEqual(self.sale.cashier.username, 'cashier')

    def test_sale_item_creation(self):
        self.assertEqual(self.sale_item.product.name, 'Test Product')
        self.assertEqual(self.sale_item.quantity, 2)
        self.assertEqual(self.sale_item.price, 100)

class SaleViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cashier', password='12345')
        self.client.login(username='cashier', password='12345')
        self.sale = Sale.objects.create(total_amount=200, payment_method='cash', cashier=self.user)

    def test_sale_list_view(self):
        response = self.client.get(reverse('sales:sale-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sale_list.html')

    def test_sale_detail_view(self):
        response = self.client.get(reverse('sales:sale-detail', args=[self.sale.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/sale_detail.html')