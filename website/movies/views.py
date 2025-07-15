from django.shortcuts import render
from . models import Movies
from cinemas.models import Cinemas
from showtimes.models import Showtimes
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils import timezone
# Create your views here.


class MovieView(ListView):
    template_name = 'movies/movies_home.html'
    model = Movies

    def get_queryset(self):
        search_request = self.request.GET.get('search')
        choisen_filters = self.request.GET.get('genre')
        queryset = Movies.objects.all()
        if search_request:
            queryset = queryset.filter(title__icontains=search_request)
        if choisen_filters:
            queryset = queryset.filter(genre__icontains=choisen_filters)
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context






def movie_detail(request, movie_slug):
    data = {'movie': Movies.objects.get(slug = movie_slug)}
    return render(request, 'movies/movie_detail.html', data)


@login_required
def buy_ticket(request, movie_slug):
    movie =  Movies.objects.get(slug=movie_slug)
    data = {
    'movie': movie,
    'cinemas': Cinemas.objects.all(),
    'showtimes': Showtimes.objects.filter(movie=movie, time__gte=timezone.localdate()),
    }
    
    return render(request, 'movies/movie_order.html', data)