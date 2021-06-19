from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Profile

class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your firstName'})
        self.fields['lastName'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your lastName'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Email'})
        self.fields['Age'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Age'})
        self.fields['Gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['Desc'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Description Here'})
        # self.fields['img'].widget.attrs.update({'class': 'form-control'})

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Enter Your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Re-Enter Your Password'})


