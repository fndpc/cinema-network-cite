from django.shortcuts import render
from . models import Cinemas, Hall
from django.views.generic import ListView
from django.conf.global_settings import YMAPS_API_KEY
def cinemas(request):
    data = {
        'cinemas': Cinemas.objects.prefetch_related('halls').all(),
        'api-link': f"https://api-maps.yandex.ru/v3/?apikey={YMAPS_API_KEY}&lang=ru_RU"
    }

    return render(request, 'cinemas/cinemas.html', data)
