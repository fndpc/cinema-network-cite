from django.urls import path, include

from mysite import settings
from . import views

urlpatterns = [
    path('', views.movies_home, name='movies'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('<int:id>/buy-ticket/', views.movie_detail, name='buy_ticket')
]
