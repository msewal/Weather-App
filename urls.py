from django.urls import path
from .views import weather_view

urlpatterns = [
    path('weather/<str:city>/', weather_view, name='weather-view'),
]
