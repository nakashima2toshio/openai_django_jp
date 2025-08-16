from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from todo_task.models import Task
from todo_task.forms import TaskForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.views import LoginView


# class CustomLoginView(LoginView):
#     template_name = 'todo_task/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse('todo_task:task_list')
#
# from django.contrib.auth.views import LogoutView
#
# class CustomLogoutView(LogoutView):
#     template_name = 'todo_task/logout.html'
#
#     def get_next_page(self):
#         return reverse_lazy('todo_task:login')


class TaskListView(LoginRequiredMixin, ListView):  # LoginRequiredMixin,
    model = Task
    template_name = 'todo_task/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):  # LoginRequiredMixin,
    model = Task
    form_class = TaskForm
    template_name = 'todo_task/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):  # LoginRequiredMixin,
    model = Task
    template_name = 'todo_task/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateView(UpdateView):  # LoginRequiredMixin,
    model = Task
    form_class = TaskForm
    template_name = 'todo_task/task_update.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(DeleteView):  # LoginRequiredMixin,
    model = Task
    template_name = 'todo_task/task_confirm_delete.html'
    success_url = reverse_lazy('todo_task:task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskAboutView(TemplateView):  # LoginRequiredMixin,
    model = Task
    template_name = 'todo_task/task_about.html'
    success_url = reverse_lazy('todo_task:task_list')
