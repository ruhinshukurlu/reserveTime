from django.shortcuts import render
from django.views.generic import TemplateView
from restaurant.models import *
from django.views.generic import DetailView, UpdateView, FormView , DeleteView
from django.views.generic.edit import FormMixin
from core.forms import *
# Create your views here.

def home(request):
    return render(request, 'home-page.html')

class HomeView(TemplateView):
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        
        return context


class CompanyProfile(FormMixin,DetailView):
    model = Company
    template_name = 'company-profile.html'
    context_object_name = 'company'
    form_class = FindTableForm


    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        # table = form.save(commit=False)
        # comment.story = get_object_or_404(Story, pk=self.kwargs.get('pk'))
        # comment.save()
        return super().form_valid(form)


class FindTableView(DetailView):
    model = Time
    context_object_name = 'times'
    template_name='company-profile.html'