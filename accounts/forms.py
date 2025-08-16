from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser

# CustomUser = get_user_model()


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
