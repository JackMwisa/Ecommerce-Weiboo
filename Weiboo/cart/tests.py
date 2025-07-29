from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from store.models import Category, Product
from cart.models import Cart, CartItem

User = get_user_model()

class CartTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cartuser', password='pass1234')
        self.category = Category.objects.create(name='Tech')
        self.product = Product.objects.create(name='Phone', category=self.category, price=100, stock=10)

    def test_add_to_cart_redirects(self):
        self.client.login(username='cartuser', password='pass1234')
        response = self.client.get(reverse('cart:add', args=[self.product.id]))
        self.assertRedirects(response, reverse('cart:detail'))

    def test_cart_requires_login(self):
        response = self.client.get(reverse('cart:detail'))
        self.assertRedirects(response, '/accounts/login/?next=/cart/')
