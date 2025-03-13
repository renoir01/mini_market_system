from django.test import TestCase
from django.urls import reverse
from .models import Product
from .forms import ProductForm

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=100, stock_level=10)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.stock_level, 10)

class ProductFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test Product', 'description': 'Test Description', 'price': 100, 'stock_level': 10}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'description': 'Test Description', 'price': 100, 'stock_level': 10}
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())

class ProductViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=100, stock_level=10)

    def test_product_list_view(self):
        response = self.client.get(reverse('inventory:product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/product_list.html')

    def test_product_add_view(self):
        response = self.client.get(reverse('inventory:product-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/product_form.html')