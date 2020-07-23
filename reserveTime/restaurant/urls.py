from django.urls import path
from restaurant.views import RestaurantRegisterView
app_name = 'restaurant'

urlpatterns = [
    path('register/restaurant', RestaurantRegisterView.as_view(), name='register_restaurant')
]