from django.shortcuts import render
from django.views.generic import TemplateView
from restaurant.models import *
from django.views.generic import DetailView, UpdateView, FormView , DeleteView

# Create your views here.

def home(request):
    return render(request, 'home-page.html')

class HomeView(TemplateView):
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        
        return context


class CompanyProfile(DetailView):
    model = Company
    template_name = 'company-profile.html'
    context_object_name = 'company'