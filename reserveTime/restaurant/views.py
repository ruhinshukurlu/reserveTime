from django.shortcuts import render, redirect
from django.views.generic import CreateView
from account.models import User
from account.forms import RestaurantRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.

class RestaurantRegisterView(CreateView):
    model = User
    form_class = RestaurantRegisterForm
    template_name = 'register-restaurant.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('core:home')
