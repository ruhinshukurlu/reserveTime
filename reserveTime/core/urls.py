from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('home', HomeView.as_view() , name='home'),
]