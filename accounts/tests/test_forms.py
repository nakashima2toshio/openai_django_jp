# accounts/tests/test_forms.py
import logging

from django.test import TestCase
from accounts.forms import SignupForm
from accounts.models import CustomUser

logger = logging.getLogger(__name__)


class SignupFormTest(TestCase):
    def test_signup_form_valid(self):
        form = SignupForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_due_to_missing_fields(self):
        form = SignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_signup_form_invalid_due_to_password_mismatch(self):
        form = SignupForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'differentpassword',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
