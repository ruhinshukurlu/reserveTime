from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from account.models import User
from account.forms import RestaurantRegisterForm, UserEditForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, FormView , DeleteView
from django.views.generic.edit import FormMixin
from restaurant.models import *
from restaurant.forms import *
from django.contrib import messages
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



class MenuView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'company-menus.html'
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        form.instance.company = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menus"] = Menu.objects.all()
        context["menu_categories"] = MenuCategory.objects.all()
        
        return context


class MenuUpdateView(UpdateView):
    model = Menu
    template_name = "menu-detail.html"
    form_class = MenuForm

    def get_success_url(self):
        return reverse_lazy('restaurant:menu')



class MenuDeleteView(DeleteView):
    model = Menu
    template_name = "menu-detail.html"
    
    def get_success_url(self):
        return reverse_lazy('restaurant:menu')


class PhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'company-photos.html'
    success_url = reverse_lazy('restaurant:photo')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photo.objects.all()
        
        return context


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = "photo-detail.html"
    form_class = PhotoForm
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse_lazy('restaurant:photo')
    

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = "photo-detail.html"
    
    def get_success_url(self):
        return reverse_lazy('restaurant:photo')


class CompanyInfosView(UpdateView):
    model = Company
    template_name = "company-infos.html"
    form_class = CompanyInfosForm
    context_object_name = 'company'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("restaurant:company-infos", kwargs={'pk': self.object.pk})


class CompanyTablesView(CreateView):
    model = Table
    template_name = 'company-tables.html'
    form_class = TableForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        inside_tables = Table.objects.filter(table_place = 'inside').order_by('size')
        outside_tables = Table.objects.filter(table_place = 'outside').order_by('size')
        return render(request, self.template_name, {'form' : form, 'inside_tables' : inside_tables, 'outside_tables' : outside_tables})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            size = form.cleaned_data['size']
            place = form.cleaned_data['table_place']

            for i in range(amount): 
                table = Table.objects.create(size = size, table_place = place, company = self.request.user)

            return HttpResponseRedirect(reverse_lazy('restaurant:company-tables', kwargs={'pk': self.request.user.pk}))

        return render(request,self.template_name, {'form' : form})

    