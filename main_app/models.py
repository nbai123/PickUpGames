from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import SignupForm

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    homecourt = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # instance.profile.height = SignupForm.height
    # print(instance.profile.height)
    instance.profile.save()

class Park(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    courts = models.IntegerField()
    space = models.CharField(max_length=100)
    schedule = models.CharField(max_length=250)

class Game(models.Model):
    location = models.OneToOneField(Park, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    count = models.IntegerField()