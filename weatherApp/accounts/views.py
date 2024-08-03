from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .signals import User
from .models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = authenticate(username=username, password=password)
        if username:
            login(request, username)
            return redirect('main')
        else:
            messages.error(request, "Oturum açılamadı, lütfen tekrar deneyiniz.")
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        tel = request.POST.get('tel')

        if password != password2:
            messages.error(request, "Şifreler uyuşmuyor!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı başka bir hesap tarafından kullanılıyor! Lütfen yeni bir tane oluşturunuz.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu mail adresi başka bir hesap adına kayıtlı!")
            return redirect('register')
        
        if User.objects.filter(tel=tel).exists():
            messages.error(request, "Bu mail adresi başka bir hesap adına kayıtlı!")
            return redirect('register')

        username = User.objects.create_user(username=username, email=email, password=password)
        username.save()
        data = User(username=username, tel=tel)
        data.save()
        login(request, username)
        return redirect('main')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')