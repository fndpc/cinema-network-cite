from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Orders
from showtimes.models import Showtimes

def orders(request, movie_id, cinema_id, showtime_id):
    order = Orders(showtime=Showtimes.objects.get(id=showtime_id), user=request.user)
    order.save()
    return render(request, 'orders/success.html', {'order': order.id})

