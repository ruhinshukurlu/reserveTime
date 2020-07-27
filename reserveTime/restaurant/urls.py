from django.urls import path
from restaurant.views import *

app_name = 'restaurant'

urlpatterns = [
    path('company/register', RestaurantRegisterView.as_view(), name='company-regsiter'),
    
]