from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import LoginForm, RegistrationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied
from orders.models import Orders
import uuid



# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('/')

def profile(request, id):
    print(id)
    if request.user.id == id:
        return render(request, 'users/profile.html', {'username': request.user.username,
                                                      'orders': Orders.objects.filter(user=request.user)})
    return PermissionDenied()


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        respones = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return respones
    
class LoginUser(LoginView):
    template_name = 'users/authorisation.html'
    authentication_form = LoginForm
    next_page = '/'
    print