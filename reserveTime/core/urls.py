from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path("company/profile/<int:pk>", CompanyProfile.as_view(), name="company-profile"),
    path("company/<int:pk>/filter", CommentFilterView.as_view(), name="comment-filter"),
    path("user/<int:pk>/savedRestaurants", SavedRestaurantsView.as_view(), name="user-saved-restaurants"),
    path("companies/<city_location>", CompanyCategoryList.as_view(), name="city-categories")
]