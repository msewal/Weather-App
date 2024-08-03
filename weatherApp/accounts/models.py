from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=12, verbose_name="Phone Number")

    def __str__(self):
        return f"{self.username.username} - {self.tel}"


