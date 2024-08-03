from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile 

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=8, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(min_length=8, label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    tel = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'tel']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu e-posta adresi zaten kullanılıyor.")
        return email

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if User.objects.filter(profile__tel=tel).exists():
            raise forms.ValidationError("Bu telefon numarası zaten kullanılıyor.")
        return tel

    def save(self, commit=True):
        username = super().save(commit=False)
        username.email = self.cleaned_data['email']
        if commit:
            username.save()
            # Profil modelini burada güncellemelisiniz
            Profile.objects.create(username=username, tel=self.cleaned_data['tel'])
        return username


#######################################################################################################
