# accounts/tests/test_models.py
from django.test import TestCase
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse
import logging

"""
1. userの登録 post - user@email.com/ password
2. login
3. logout
4. userの削除 
"""
logger = logging.getLogger(__name__)


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(username='superuser', email='superuser@example.com', password='testpassword123')
        self.assertEqual(superuser.username, 'superuser')
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertTrue(superuser.check_password('testpassword123'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py test accounts.tests.test_models
