from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import BlogPost

User = get_user_model()

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass1234')
        self.post = BlogPost.objects.create(author=self.user, title='Test Post', content='Test content')

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog:blog_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test content')
