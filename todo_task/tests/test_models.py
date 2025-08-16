# todo_task/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from todo_task.models import Task
from datetime import date


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            due_date=date.today(),
            completed=False
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task.')
        self.assertEqual(task.due_date, date.today())
        self.assertFalse(task.completed)
        self.assertEqual(task.user.username, 'testuser')

    def test_task_creation_with_blank_fields(self):
        task = Task.objects.create(
            user=self.user,
            title='Test Task with Blank Fields'
        )
        self.assertEqual(task.title, 'Test Task with Blank Fields')
        self.assertIsNone(task.description)
        self.assertIsNone(task.due_date)
        self.assertFalse(task.completed)
        self.assertEqual(task.user.username, 'testuser')

    def test_task_string_representation(self):
        task = Task.objects.create(
            user=self.user,
            title='String Representation Test'
        )
        self.assertEqual(str(task), 'String Representation Test')

    def test_task_field_validation(self):
        with self.assertRaises(ValueError):
            task = Task.objects.create(
                user=self.user,
                title='x' * 256  # Exceeding max_length
            )
