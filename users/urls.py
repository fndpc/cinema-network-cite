from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('register/', views.RegistrationView.as_view(), name = 'register'),
    path('logout/', views.user_logout, name = 'logout'),
    path('<int:id>/', views.profile, name = 'profile')
]
