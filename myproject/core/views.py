from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, UpdateView

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


class ProfileEditView(UpdateView):
    model = CustomUser
    template_name = 'core/edit_profile.html'
    pk_url_kwarg = 'user_id'
    fields = ['first_name', 'last_name', 'email', 'birth_date', 'about', 'avatar', 'phone_number']

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['header'] = f'Update profile of {object.username}'
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object != request.user:
            raise PermissionDenied("You can't edit this profile info!")

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        object = self.get_object()
        return reverse('core:profile', kwargs={'user_id': object.id})


class AddFriendView(View):
    http_method_names = ['post', ]

    def post(self, request, user_id, *args, **kwargs):
        friend = get_object_or_404(CustomUser, id=user_id)
        me = request.user

        if me.friends.filter(id=friend.id).exists():
            me.friends.remove(friend)
        else:
            me.friends.add(friend)
        return redirect(request.META.get('HTTP_REFERER'), request)


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("core:password_reset_done")
    template_name = "core/password_reset/password_reset_form.html"
    email_template_name = "core/password_reset/password_reset_email.html"
    subject_template_name = "core/password_reset/subject_template_name.txt"


class CustomPasswordResetViewDone(PasswordResetDoneView):
    template_name = "core/password_reset/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("core:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "core/password_reset/password_reset_complete.html"
