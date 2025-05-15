from django.shortcuts import render
from orders.models import Orders
from showtimes.models import Showtimes

def orders(request):
    if request.method == 'POST':
        print(f"-------------------------{request.POST['showtime']}------------")
        showtime = Showtimes.objects.get(pk = request.POST['showtime'])
        user = request.user
        order = Orders(showtime=showtime, user=user)
        order.save()
        return render(request, 'orders/success.html')
    return render(request, 'orders/fail.html')

