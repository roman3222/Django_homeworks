from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    date_now = datetime.datetime.now()
    time = date_now.strftime('%H:%M')
    msg = f'Текущее время: {time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        dir = os.getcwd()
        file = os.listdir(dir)
        file_str  = ' - '.join(file)
        return HttpResponse(file_str)
    except:
        raise NotImplemented

