from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from account.models import User
from restaurant.models import *

class CompanyEditForm(forms.ModelForm):
    profile_img = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control height',
                'placeholder' : 'First Name',
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control height',
                'placeholder' : 'Last Name',
                }),
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control height',
                'placeholder' : 'Email'
            }),
        }

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('title','price','description','menu_type',)

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Price'
            }),
            'menu_type' : forms.Select(attrs={
                'class' : 'form-control',
                'placeholder' : 'Type'
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Write description ...',
                'rows' : '5'
            })
        }

class PhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        fields = ("photo",'photo_url','photo_type',)

        widgets = {
            
            'photo_url' : forms.TextInput(attrs={
                # 'class' : 'form-control',
                'placeholder' : 'Photo Url',
                'required' : 'False'
            }),
            'menu_type' : forms.Select(attrs={
                'class' : 'select-img-type',
                'placeholder' : 'Type'
            })
        }