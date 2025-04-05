from django.shortcuts import render
from django.http import HttpResponse
from . models import Movies
from . forms import OrderForm


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
    if request.method == 'POST':
        form = OrderForm(request.POST)
    else:
        form = OrderForm()
    return render(request, 'movies/movie_order.html', {'form': form})