# weatherApp/weather/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Ana weather sayfası
    path('settings/', views.settings, name='settings'),  # Ayarlar sayfası
    # Diğer weather URL'leri burada
]
