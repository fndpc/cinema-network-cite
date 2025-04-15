from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUser.as_view(), name='authorisation'),
    path('logout/', views.user_logout, name = 'logout'),
    path('register/', views.CreateUser.as_view(), name = 'register')

]