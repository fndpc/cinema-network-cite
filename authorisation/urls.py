from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorisation, name='authorisation'),
    path('/logout', views.user_logout, name = 'logout')

]