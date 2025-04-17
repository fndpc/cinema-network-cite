from django.shortcuts import render
from . models import Movies
from cinemas.models import Cinemas
from showtimes.models import Showtimes
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# Create your views here.


class MovieView(ListView):
    template_name = 'movies/movies_home.html'
    model = Movies

    def get_queryset(self):
        search_term = self.request.GET.get('search')
        if search_term:
            return Movies.objects.filter(title__icontains=search_term)
        return Movies.objects.all()
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context






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