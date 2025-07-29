from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product

class StoreTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(name='Django for Beginners', category=self.category, price=50, stock=5)

    def test_product_list_view(self):
        response = self.client.get(reverse('store:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django for Beginners')

    def test_product_detail_view(self):
        response = self.client.get(reverse('store:product_detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
