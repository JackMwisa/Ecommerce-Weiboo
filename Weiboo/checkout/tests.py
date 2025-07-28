from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from cart.models import Cart
from .models import Order

User = get_user_model()

class CheckoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.cart = Cart.objects.create(user=self.user)

    def test_checkout_page_requires_login(self):
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, '/accounts/login/?next=/orders/checkout/')

    def test_successful_checkout(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.post(reverse('checkout'), {
            'shipping_address': '123 Example Street',
            'billing_address': '456 Billing Ave',
        })
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.user, self.user)
        self.assertRedirects(response, reverse('checkout_success'))
