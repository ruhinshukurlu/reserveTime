from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('user/register', CustomerRegisterView.as_view(), name= 'user-register'),
    path('user/login', LoginView.as_view(), name='user-login'),
]