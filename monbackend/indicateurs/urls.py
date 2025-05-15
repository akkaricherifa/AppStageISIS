# monbackend/indicateurs/urls.py

from django.urls import path
from . import views
from .views import connexion_superadmin

urlpatterns = [
    path('', views.home, name='home'),  # Tu appelleras la vue "home"
    path('home2/', views.home2, name='home2'),
    path('interface/', views.interface, name='interface'),
    path('home2/interface/', views.interface, name='interface_from_home2'),
    path('connexion/', connexion_superadmin, name='connexion'),

    # path('admin/login/', views.connexion, name='login_superadmin'),

]
