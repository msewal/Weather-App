from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.

def main(request):
    return render(request, 'main.html')

def settings(request):
    return render(request, 'weather/settings.html') 

