
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Company,Customer

class CustomerRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # profile_image = forms.FileField('Profile', max_length=, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user

class RestaurantRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=250)
    # phone_number = forms.IntegerField()

    city_location = forms.CharField(max_length=150)
    province_location = forms.CharField(max_length=150)
    country_location = forms.CharField(max_length=150)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        company = Company.objects.create(user=user)
        # company.phone_number=self.cleaned_data.get('phone_number')
        company.company_name=self.company_name.get('company_name')
        company.city_location=self.city_location.get('city_location')
        company.save()
        return user
  