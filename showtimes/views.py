from django.shortcuts import render
from django.views.generic import ListView
from .models import Showtimes
from django.utils import timezone
from datetime import datetime, timedelta
# Create your views here.


class ShowtimesView(ListView):
    template_name = 'showtimes/showtimes.html'
    model = Showtimes


    def get_queryset(self):
        chosen_date = self.request.GET.get('date')
        today_date = timezone.localdate()
        if chosen_date:
            # Преобразуем строку в объект datetime
            chosen_date = datetime.strptime(chosen_date, '%Y-%m-%d')
            # Определяем начало и конец дня
            start_of_day = chosen_date
            end_of_day = chosen_date + timedelta(days=1)
            # Фильтруем по диапазону
            return super().get_queryset().filter(time__gte=start_of_day, time__lt=end_of_day)
        return super().get_queryset().filter(time__gte=today_date,
                                              time__lte=today_date+timedelta(days=1))
        
    

