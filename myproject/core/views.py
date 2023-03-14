from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView
# from django.views.generic.base import View

from .forms import LoginForm, SignupForm
from .models import CustomUser


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('post:index')
    extra_context = {'header': 'Login'}
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('post:index')
    http_method_names = ['post', ]


class SignupView(View):
    template_name = 'core/signup.html'
    form = SignupForm

    def get_context_data(self):
        context = {
            'header': 'Signup',
            'form': self.form,
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, request.FILES)
        context = self.get_context_data()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('post:index'))
        else:
            return render(request, self.template_name, context)


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'core/profile.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['header'] = f'Profile of {object.username}'
        return context
