# todo_task/models.py
# todo_task/models.py
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # この行を追加


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if len(self.title) > 255:
            raise ValueError("タイトルの長さが最大長を超えています！")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """タスク詳細ページのURLを返す"""
        return reverse('todo_task:task_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
