# accounts/views.py
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import SignupForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


@login_required
def login_view(request):
    return render(request, 'accounts/login.html')


def logout_view(request):
    return render(request, 'accounts/logout.html')


class SignupView(CreateView):
    """ form_validがない場合は、ユーザー登録後は、ログイン画面にリダイレクトさせ、ユーザーに手動でログインさせる """
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """ ユーザー登録後に自動でログインさせる """
        # self.objectにsave()されたUserオブジェクトが入る
        valid = super().form_valid(form)
        # user = form.save()
        login(self.request, self.object)
        return valid


@login_required
class LoginView(CreateView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('profile')
