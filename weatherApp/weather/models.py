from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=150)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    hunidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()


