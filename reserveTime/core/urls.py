from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path("company/profile/<int:pk>", CompanyProfile.as_view(), name="company-profile"),
    path("company/profile/<int:pk>/table", FindTableView.as_view(), name="company-table"),
]