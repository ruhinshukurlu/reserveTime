from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, HttpResponseRedirect
from restaurant.models import *
from django.views.generic import DetailView,TemplateView, ListView, UpdateView, FormView , DeleteView, View
from django.views.generic.edit import FormMixin, FormView
from core.forms import *
from django.shortcuts import get_list_or_404, get_object_or_404 
import datetime
from django.views.decorators.csrf import csrf_exempt



class HomeView(TemplateView):
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context

    
class CompanyProfile(FormMixin, DetailView):
    model = Company
    template_name = 'company-profile.html'
    form_class = FindTableForm
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = Company.objects.filter(pk=self.kwargs.get('pk'))

        company_photos = Photo.objects.filter(owner=company.first().user)
        context['photos'] = company_photos
        
        menu_categories = MenuCategory.objects.all()
        context['menu_categories'] = menu_categories

        menus = Menu.objects.filter(company = company.first().user)
        context['menus'] = menus

        comments = Comment.objects.filter(company = company.first()).distinct('user')
        context['comments'] = comments
        
        context['users'] = User.objects.all()

        saved_restaurant = SavedRestaurant.objects.filter(company=company.first(), user= self.request.user)
        context['saved_restaurant'] = saved_restaurant.first()            

        company_start_hour = company.values('work_hours_from').first().get('work_hours_from')
        company_finish_hour = company.values('work_hours_to').first().get('work_hours_to')
        
        free_times = []
        free_times.append(company_start_hour)
        while company_start_hour < company_finish_hour:
            company_start_hour = (datetime.datetime.combine(  
                    datetime.date(1, 1, 1),  
                    company_start_hour
                ) + datetime.timedelta(minutes=30)).time()

            free_times.append(company_start_hour)
        
        free_times = free_times[:-1]
        context["work_hours"] = free_times

        reserve_start_date = datetime.date.today()
        reserve_finish_date = (datetime.date.today()+datetime.timedelta(days=30)).isoformat()
        context['reserve_start_date'] = reserve_start_date
        context['reserve_finish_date'] = reserve_finish_date

        inside_tables = Table.objects.filter(company=company.values('user').first().get('user'), table_place='inside')
        outside_tables = Table.objects.filter(company=company.values('user').first().get('user'), table_place='outside')  

        inside_tables_sizes = []
        outside_tables_sizes = []

        for table in inside_tables:
            if table.size not in inside_tables_sizes:
                inside_tables_sizes.append(table.size)
        
        for table in outside_tables:
            if table.size not in outside_tables_sizes:
                outside_tables_sizes.append(table.size)

        context['inside_tables_sizes'] = inside_tables_sizes
        context['outside_tables_sizes'] = outside_tables_sizes

        menus = Menu.objects.filter(company=company.values('user').first().get('user'))
        context['menus'] = menus
        context['menu_categories'] = MenuCategory.objects.all()
        
        reserve_dates = []

        for i in range(31):
            reserve_dates.append(reserve_start_date)
            reserve_start_date = (reserve_start_date+datetime.timedelta(days=1))
        
        
        return context
       

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
                
            if request.POST.get('form_id') == 'FindTableForm':
                company = Company.objects.filter(pk=self.kwargs.get('pk'))
                print(request.POST)
                party_size = request.POST.get('size')
                reserve_date = request.POST.get('date')
                reserve_time = request.POST.get('time')
                table_place = request.POST.get('table_place')
                # print(reserve_date)
                party_size = int(party_size)
                reserve_date_obj = datetime.datetime.strptime(reserve_date, '%Y-%m-%d')
                reserve_time_obj = datetime.datetime.strptime(reserve_time, '%H:%M:%S').time()

                reserve_start_date = datetime.date.today()
                reserve_finish_date = (datetime.date.today()+datetime.timedelta(days=30)).isoformat()
            
                reserve_dates = []
                for i in range(31):
                    reserve_dates.append(reserve_start_date)
                    reserve_start_date = (reserve_start_date+datetime.timedelta(days=1))

                response_data = {}
                
                date = TableDate.objects.filter(date=reserve_date_obj)
                tables = Table.objects.filter(company=company.values('user').first().get('user'), dates__in=date, table_place=table_place, size=party_size)   

                # print(tables)   
                
                for table in tables:
                    times = table.times.filter(reserved=False)
                    for time in times:
                        if reserve_time_obj == time.free_time:
                            found_result = {
                                'table' : table,
                                'time' : time.free_time,
                                'time_id' : time.id,
                                'table_size' : party_size,
                                'table_id' : table.id,
                                'table_place' : table.table_place,
                                'reserved_date' : reserve_date_obj
                            }
                            response_data['found_result'] = found_result
                            
                            break
                        else:
                            response_data['not_found'] = 'We dont have any table in the particular time...'

               

                return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )

            elif request.POST.get('form_id') == 'selectMenuForm':
                company = Company.objects.filter(pk=self.kwargs.get('pk'))

                # print(request.POST)
                reserve_date = request.POST.get('reserve_date')
                reserve_time = request.POST.get('reserve_time')
                table_id = request.POST.get('table_id')
                table = Table.objects.filter(pk=table_id)

                reserve_date_obj = datetime.datetime.strptime(reserve_date, '%Y-%m-%d')
                reserve_time_obj = datetime.datetime.strptime(reserve_time, '%H:%M:%S').time()
                total_price = request.POST.get('total_price')

                date = TableDate.objects.filter(date=reserve_date_obj)
                table = Table.objects.filter(pk=table_id, dates__in=date)
                
                table.first().times.filter(free_time=reserve_time_obj).update(reserved = True)

                response_data = {
                   
                }

                reservation = Reservation.objects.create(
                    user=request.user, 
                    company=company.first(), 
                    table_id=table_id, 
                    reserved_time= reserve_time_obj,
                    reserved_date=reserve_date_obj,
                    total_price = total_price
                )   
                
                for i in range(0,int(request.POST.get('length'))):
                    menu_id = int(request.POST.get(f'selected_menus_list[{i}][menu_id]'))
                    portion_count = int(request.POST.get(f'selected_menus_list[{i}][portion_count]'))

                    portion = Portion.objects.create(menu_id=menu_id, portion_count=portion_count)
                    reservation.portions.add(portion)
                    
            
                return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )
            
            elif request.POST.get('form_id') == 'saveRestaurantForm':
                company = Company.objects.filter(pk=self.kwargs.get('pk'))

                response_data = {}

                if(SavedRestaurant.objects.filter(user=request.user, company=company.first())):
                    saved_restaurant = SavedRestaurant.objects.filter(company=company.first(), user=request.user)
                    if saved_restaurant.first().saved:
                        saved_restaurant.update(saved=False)
                        response_data['saved'] = 'false'
                    else:
                        saved_restaurant.update(saved=True)
                        response_data['saved'] = 'true'
                else:
                    saved_restaurant = SavedRestaurant.objects.create(company=company.first(), user=request.user, saved=True)
                    response_data['saved'] = 'true'

                

                return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )

            
        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )

        
class SavedRestaurantsView(ListView):
    template_name = "user-saved-restaurants.html"
    context_object_name = 'saved_restaurants'
    
    def get_queryset(self):
        return SavedRestaurant.objects.filter(user=self.request.user, saved=True)
    

