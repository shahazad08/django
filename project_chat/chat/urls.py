# chat/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('home/', views.home, name='index'),
    re_path(r'(?P<room_name>[^/]+)/$', views.room, name='room'),
]