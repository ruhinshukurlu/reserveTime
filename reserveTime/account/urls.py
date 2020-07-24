from django.urls import path
from account.views import *
from django.contrib.auth.views import LogoutView

app_name = 'account'

urlpatterns = [
    path('user/register', CustomerRegisterView.as_view(), name= 'user-register'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
]