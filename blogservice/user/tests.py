from django.test import TestCase, Client
from django.urls import reverse

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('user:register')
        self.user_data = {
            'email': 'testuser@example.com',
            'name': 'test',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

    def test_user_registration_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')

    def test_user_registration_view_post(self):
        response = self.client.post(self.register_url, self.user_data, follow=True)
        self.assertRedirects(response, reverse('user:verification_sent'))
