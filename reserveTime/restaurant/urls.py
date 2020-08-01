from django.urls import path
from restaurant.views import *

app_name = 'restaurant'

urlpatterns = [
    path('company/register', RestaurantRegisterView.as_view(), name='company-regsiter'),
    path("company/menus", MenuView.as_view(), name="menu"),
    path("company/photos", PhotoView.as_view(), name="photo")
]