from django.urls import path, include

from mysite import settings
from . import views

urlpatterns = [
    path('', views.movies_home, name='movies'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('<int:id>/buy-ticket/', views.buy_ticket, name='buy_ticket')
]
