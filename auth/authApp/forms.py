from django import forms
from django.forms import ModelForm, TextInput

class UserAuthForm(forms.Form):
    userName = forms.CharField(label='Имя пользователя:')
    userPassword = forms.CharField(label='Пароль:')