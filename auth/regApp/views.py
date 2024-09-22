from django.shortcuts import render, redirect
from .forms import *
from domain.views import encrypt_password
from domain.models import User

def signup(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = encrypt_password(password)
            user_email = form.cleaned_data['user_email']
            User.objects.create(username = username, password = password, user_email=user_email)
            return redirect('signin')
    return render(request,'reg_index.html', {'reg_auth_form' : UserForm})
