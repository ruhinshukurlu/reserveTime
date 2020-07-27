from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from account.models import User


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
