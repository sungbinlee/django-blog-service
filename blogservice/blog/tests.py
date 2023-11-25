from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, User


class PostListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
