from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Account


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('phone_number', 'password')

    def clean(self):
        if self.is_valid():
            phone_number = self.cleaned_data['phone_number']
            password = self.cleaned_data['password']
            if not authenticate(phone_number=phone_number, password=password):
                raise forms.ValidationError("Invalid login")


class RegistrationForm(UserCreationForm):
    phone_number = forms.IntegerField(help_text='Required. Add a valid number.', required=True)

    class Meta:
        model = Account
        fields = ['phone_number',
                  'full_name',
                  'd_o_b',
                  'email',
                  'passport_number',
                  'image',
                  'password1',
                  'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['phone_number',
                  'full_name',
                  'd_o_b',
                  'email',
                  'passport_number',
                  'image'
                  ]
