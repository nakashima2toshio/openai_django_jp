from django import forms
from todo_task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'due_date', 'completed']


# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
#
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
