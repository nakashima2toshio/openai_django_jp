# todo_task/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from todo_task.models import Task
from datetime import date


class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            due_date=date.today(),
            completed=False
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('todo_task:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_list.html')
        self.assertIn('tasks', response.context)

    def test_task_create_view(self):
        response = self.client.get(reverse('todo_task:task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_create.html')
        form_data = {
            'title': 'New Task',
            'description': 'This is a new task.',
            'due_date': date.today(),
            'completed': False
        }
        response = self.client.post(reverse('todo_task:task_create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_detail_view(self):
        response = self.client.get(reverse('todo_task:task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_detail.html')
        self.assertIn('object', response.context)
        self.assertEqual(response.context['object'].title, 'Test Task')

    def test_task_update_view(self):
        response = self.client.get(reverse('todo_task:task_update', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_update.html')
        form_data = {
            'title': 'Updated Task',
            'description': 'This is an updated task.',
            'due_date': date.today(),
            'completed': True
        }
        response = self.client.post(reverse('todo_task:task_update', args=[self.task.id]), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete_view(self):
        response = self.client.get(reverse('todo_task:task_confirm_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_confirm_delete.html')
        response = self.client.post(reverse('todo_task:task_confirm_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_task_about_view(self):
        response = self.client.get(reverse('todo_task:task_about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_task/task_about.html')
