# monbackend/indicateurs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Tu appelleras la vue "home"
    path('home2/', views.home2, name='home2'),
    path('interface/', views.interface, name='interface'),
]
