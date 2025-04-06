from django.shortcuts import render

# Create your views here.
def showtimes(request):
    return render(request, 'showtimes/showtimes.html')