from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowtimesView.as_view(), name = 'showtimes')
]
