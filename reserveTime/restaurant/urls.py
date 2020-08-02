from django.urls import path
from restaurant.views import *

app_name = 'restaurant'

urlpatterns = [
    path('company/register', RestaurantRegisterView.as_view(), name='company-regsiter'),
    path("company/menus", MenuView.as_view(), name="menu"),
    path("company/menus/<int:pk>/update", MenuUpdateView.as_view(), name="menu-update"),
    path("company/menus/<int:pk>/delete", MenuDeleteView.as_view(), name="menu-delete"),
    path("company/photos", PhotoView.as_view(), name="photo"),
    path("company/photos/<int:pk>/update", PhotoUpdateView.as_view(), name="photo-update"),
    path("company/photos/<int:pk>/delete", PhotoDeleteView.as_view(), name="photo-delete"),
    path("company/<int:pk>/informations", CompanyInfosView.as_view(), name="company-infos"),
    path("company/<int:pk>/tables", CompanyTablesView.as_view(), name="company-tables"),
]