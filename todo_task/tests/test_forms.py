# # todo_task/tests/test_forms.py
from django.test import TestCase
from django.contrib.auth.models import User
from todo_task.forms import TaskForm
from todo_task.models import Task
from datetime import date


class TaskFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_task_form_valid(self):
        form_data = {
            'user': self.user.id,
            'title': 'Test Task',
            'description': 'This is a test task.',
            'due_date': date.today(),
            'completed': False
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_valid_required_fields(self):
        form_data = {
            'user': self.user.id,
            'title': 'Test Task'
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_missing_required_fields(self):
        form_data = {
            'description': 'This is a test task without a title.'
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_task_form_invalid_incorrect_data_types(self):
        form_data = {
            'user': self.user.id,
            'title': 'Test Task',
            'due_date': 'invalid_date'
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('due_date', form.errors)

    def test_task_form_field_properties(self):
        form = TaskForm()
        self.assertEqual(form.fields['title'].max_length, 255)
        self.assertTrue(form.fields['description'].required is False)
        self.assertTrue(form.fields['due_date'].required is False)
        self.assertTrue(form.fields['completed'].required is False)
