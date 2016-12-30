from django.shortcuts import render
import services


def home(request):
    render(request, 'rsstelegram/home', {})


def get3DJuegos(request):
    work = True
    while work:
        data = services.get3DJuegos()
        if data.get('title') is not None:
            services.sendTelegram(data)
    render(request, 'rsstelegram/home', {})
