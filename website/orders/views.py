from django.shortcuts import render
from orders.models import Orders
from urllib.parse import quote
from showtimes.models import Showtimes
from orders.services.generate_qr import make_qr
from orders.services.sender import send_tiket
import pika

def orders(request):
    if request.method == 'POST':
        showtime = Showtimes.objects.get(pk = request.POST['showtime'])
        user = request.user
        qr = make_qr(user.token, showtime.__str__())
        order = Orders(showtime=showtime, user=user, qr=qr)
        order.save()
        if user.telegram_chat_id is not None:
            send_tiket(qr_path=order.qr.path, telegram_chat_id=user.telegram_chat_id)
        return render(request, 'orders/success.html')
    return render(request, 'orders/fail.html')

