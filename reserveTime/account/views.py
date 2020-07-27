from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import DetailView, UpdateView
from account.models import User
from account.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'register-user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('core:home')

# class LoginView(LoginView):
#     template_name = 'login-user.html'
#     form_class = LoginForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         print(self.request.user)
#         return render(request, self.template_name, {'form' : form})

#     def form_valid(self, form):
#         # print(self.request.user)
#         return redirect('core:home')

def login_view(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('core:home')
    context = {"form": form}

    return render (request, "login-user.html", context)

class ChangePasswordView(PasswordChangeView):
    template_name = 'change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('core:home')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'change_password_done.html'


class CustomerProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user-profile.html'
    context_opject_name = 'user'

    def get_object(self):
        return self.request.user

class CustomerUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-edit.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account:user-profile', kwargs={'pk': self.object.pk})


class CompanyProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'company-admin-page.html'
    context_opject_name = 'user'

    def get_object(self):
        return self.request.user

class CompanyUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-edit.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return redirect('restaurant:company-profile', kwargs={'pk': self.object.pk})