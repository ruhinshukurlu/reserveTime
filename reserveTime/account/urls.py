from django.urls import path
from account.views import CustomerRegisterView

app_name = 'account'

urlpatterns = [
    path('register/user', CustomerRegisterView.as_view(), name= 'register_user')
]