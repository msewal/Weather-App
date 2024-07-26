from django.http import JsonResponse
from .utils import get_weather

def weather_view(request, city):
    weather_data = get_weather(city)
    return JsonResponse(weather_data)
