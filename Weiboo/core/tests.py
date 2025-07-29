from django.test import TestCase
from django.urls import reverse

class CoreTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)
