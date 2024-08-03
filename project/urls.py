# project/urls.py
from django.contrib import admin
from django.urls import path, include
from weatherApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('weatherApp.accounts.urls')),  # accounts URL'lerini include edin
    path('weather/', include('weatherApp.weather.urls')),    # weather URL'lerini include edin
    path('', views.main, name='main'),  # Home Page    
    ]
