from django.shortcuts import render, redirect
from . forms import AuthForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
def authorisation(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
                return render(request, 'authorisation/authorisation.html', {'form': form})
    else:
        form = AuthForm()
    return render(request, 'authorisation/authorisation.html', {'form': form})

class Logout(LogoutView):
     next_page = reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = User(username = form.cleaned_data['username'])
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = AuthForm()
    return render(request, 'authorisation/registration.html', {'form': form})


class Login(LoginView):
    template_name = 'authorisation/authorisation.html'
    authentication_form = AuthForm
    next_page = '/'