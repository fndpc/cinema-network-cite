from django.shortcuts import render
from django.http import HttpResponse
from . models import Movies
from . forms import OrderForm
from cinemas.models import Cinemas
from showtimes.models import Showtimes
from django.contrib.auth.decorators import login_required
# Create your views here.
def movies_home(request):
    data = {
        'movies': Movies.objects.all()
    }
    return render(request, 'movies/movies_home.html', data)


def movie_detail(request, movie_slug):
    data = {'movie': Movies.objects.get(slug = movie_slug)}
    return render(request, 'movies/movie_detail.html', data)


@login_required
def buy_ticket(request, movie_slug):
    movie = Movies.objects.get(slug=movie_slug)
    data = {'movie': movie,
            'cinemas': Cinemas.objects.all(),
            'showtimes': Showtimes.objects.filter(movie=movie.id)}
    return render(request, 'movies/movie_order.html', data)