from django.shortcuts import render, redirect
from . forms import AuthForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def authorisation(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = AuthForm()
    return render(request, 'authorisation/authorisation.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('/')