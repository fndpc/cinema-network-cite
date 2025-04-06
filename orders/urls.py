from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/<int:cinema_id>/<int:showtime_id>/', views.orders, name='orders')
]
