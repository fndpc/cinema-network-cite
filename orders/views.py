from django.shortcuts import render
from orders.models import Orders
from urllib.parse import quote
from showtimes.models import Showtimes
from orders.services.generate_qr import make_qr
import pika

def orders(request):
    if request.method == 'POST':
        showtime = Showtimes.objects.get(pk = request.POST['showtime'])
        user = request.user
        qr = make_qr(user.token, showtime.__str__())
        order = Orders(showtime=showtime, user=user, qr=qr)
        order.save()
        if user.telegram_chat_id is not None:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='hello')
        return render(request, 'orders/success.html')
    return render(request, 'orders/fail.html')

