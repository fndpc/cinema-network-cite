from django.shortcuts import render
from orders.models import Orders
from urllib.parse import quote
from showtimes.models import Showtimes
from telegram_bot.bot import send_notiflication

def orders(request):

    if request.method == 'POST':
        showtime = Showtimes.objects.get(pk = request.POST['showtime'])
        user = request.user
        order = Orders(showtime=showtime, user=user)
        order.save()
        send_notiflication(order) # Отправка сообщения в тг бота
        return render(request, 'orders/success.html')
    return render(request, 'orders/fail.html')

