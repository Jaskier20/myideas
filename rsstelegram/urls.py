from django.conf.urls import url
from rsstelegram import views

urlpatterns = [
    url(r'^get3djuegos/', views.get3DJuegos, name='get-3djuegos'),
    url(r'^Home/', views.home, name='home'),
]
