from django.urls import path, include

urlpatterns = [
    path('accounts/', include('weatherApp.accounts.urls')),  # Accounts uygulaması için URL'ler
    path('weather/', include('weatherApp.weather.urls')),    # Weather uygulaması için URL'ler
]
