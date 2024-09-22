from django import forms
from django.forms import ModelForm, TextInput, Textarea
from domain.models import *

class UserForm(ModelForm):
    class Meta:
        model =User
        fields = ['username','password','user_email']
        widgets = {
            'username': TextInput(attrs={'class':'form-control','placeholder':"Логин:"}),
            'user_email': TextInput(attrs={'class': 'form-control', 'placeholder': "E-mail:"}),
            'password': TextInput(attrs={'class': 'form-control', 'placeholder': "Пароль"}),
        }
