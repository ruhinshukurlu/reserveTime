from django.urls import path
from core.views import check

app_name = 'core'

urlpatterns = [
    path('', check , name='home'),
]