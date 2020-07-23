from django.shortcuts import render
from django.views.generic import CreateView
from account.models import User
from account.forms import CustomerRegisterForm
from django.urls import reverse_lazy
# Create your views here.

class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'register-user.html'
    success_url = reverse_lazy('core:home')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     messages.warning(self.request, 'Something went wrong!!')
    #     return super().form_invalid(form)

