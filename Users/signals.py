from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# this is for creating profile for every user that registers
@receiver(post_save, sender=User)  # this line receives if Useer is created and then the rest executes
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# this is going to save profiles when a user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
