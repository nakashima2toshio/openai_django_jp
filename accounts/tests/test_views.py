# accounts/tests/test_view.py
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com',
                                                   password='password123')
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.logout_url = reverse('logout')

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_login_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout.html')
