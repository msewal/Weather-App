from django.shortcuts import render
from weatherApp.accounts import models

def main(request):
    return render(request, 'weather/main.html')

def settings(request):
    return render(request, 'weather/settings.html')
