from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from movies.models import Movies

class HomeView(ListView):
    model = Movies
    template_name = 'home/home_page.html'
