from django.shortcuts import render
from django.views.generic import CreateView
from account.models import User
from account.forms import RestaurantRegisterForm
from django.urls import reverse_lazy
# Create your views here.

class RestaurantRegisterView(CreateView):
    model = User
    form_class = RestaurantRegisterForm
    template_name = 'register-restaurant.html'
    success_url = reverse_lazy('core:home')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
