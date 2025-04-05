from django.shortcuts import render, redirect
from . forms import AuthForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('/')

class CreateUser(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = "authorisation/registration.html"

class LoginUser(LoginView):
    template_name = 'authorisation/authorisation.html'
    authentication_form = AuthForm
    next_page = '/'