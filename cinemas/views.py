from django.shortcuts import render
from . models import Cinemas, Hall


# Create your views here.
def cinemas(request):
    data = {
        'cinemas': Cinemas.objects.prefetch_related('halls').all()
    }

    return render(request, 'cinemas/cinemas.html', data)