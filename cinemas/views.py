from django.shortcuts import render
from . models import Cinemas, Hall
from django.views.generic import ListView
# Create your views here.
def cinemas(request):
    data = {
        'cinemas': Cinemas.objects.prefetch_related('halls').all()
    }

    return render(request, 'cinemas/cinemas.html', data)
