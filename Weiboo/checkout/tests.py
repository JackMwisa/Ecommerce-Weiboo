from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from checkout.models import Order

User = get_user_model()

class CheckoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='buyer', password='pass1234')

    def test_order_list_requires_login(self):
        response = self.client.get(reverse('checkout:order_list'))
        self.assertRedirects(response, '/accounts/login/?next=/checkout/orders/')

    def test_order_list_logged_in(self):
        self.client.login(username='buyer', password='pass1234')
        response = self.client.get(reverse('checkout:order_list'))
        self.assertEqual(response.status_code, 200)
