from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Profile oluşturma işlemleri
        pass

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Profile kaydetme işlemleri
    pass
