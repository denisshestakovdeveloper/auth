from django.shortcuts import render
from .forms import *
from domain.models import *
from domain.views import decrypt_password

def auth(request):
    if request.method =='POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            password = form.cleaned_data['userPassword']
            if User.objects.filter(username=userName).exists():
                user_in_db = User.objects.filter(username = userName).first()
                if user_in_db.isUserValid(password = password):
                    res = "Вы авторизованы!"
                else:
                    res = "Пароль неверный!"
            else:
                res = "Пользователя с таким логином не существует!"
        context = {'auth_user_form': form, 'result': res}
        return render(request, 'index.html', context)

    return render(request,'index.html',{'auth_user_form':UserAuthForm})