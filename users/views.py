from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login')) # на главную страницу сайта

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
       # Display blank registration form.
       form = UserCreationForm()
    else:
       # Обработка заполненной формы.
       form = UserCreationForm(data=request.POST)
       if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            authenticated_user = authenticate(username=new_user.username, password = request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form' : form}
    return render(request, 'users/register.html', context)
       