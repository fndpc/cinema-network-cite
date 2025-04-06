from django.shortcuts import render
from django.http import HttpResponse
from . models import Movies
from . forms import OrderForm
from cinemas.models import Cinemas
from showtimes.models import Showtimes
# Create your views here.
def movies_home(request):
    data = {
        'movies': Movies.objects.all()
    }
    return render(request, 'movies/movies_home.html', data)


def movie_detail(request, id):
    data = {'movie': Movies.objects.get(pk = id)}
    return render(request, 'movies/movie_detail.html', data)



def buy_ticket(request, id):
    data = {'movie': Movies.objects.get(pk=id),
     'cinemas': Cinemas.objects.all(),
      'showtimes': Showtimes.objects.filter(movie=id)}
    return render(request, 'movies/movie_order.html', data)