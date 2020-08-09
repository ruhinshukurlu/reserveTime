from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path("company/profile/<int:pk>", CompanyProfile.as_view(), name="company-profile"),
    path("company/profile/<int:pk>/menus", SelectMenu.as_view(), name="select-menu"),
    path("company/profile/<int:pk>/reservations", ReservationListView.as_view(), name="reservation-list"),

]