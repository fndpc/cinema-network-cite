from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
def info(request):
    return render(request, 'info/info.html')

class InfoView(TemplateView):
    template_name = 'info/info.html'
    