from django.db.models.signals import post_save # post_save: sent at the end of save() method
from django.contrib.auth.models import User
from django.dispatch import receiver # receiver: function that gets the signal
from .models import Profile

# receive signal when save event occurs in the User Model - specifically listen for post_save()
# receiver: a signal/list of signals to connect a function to
# post_save: sent at the end of save() method
# sender: the model class being saved (User Model)
@receiver(post_save, sender=User)
# function will only be called when an instance of the User Model is saved
# function creates profile with the same instance being created
# signal handlers must take a sender and **kwargs
# instance: the actual instance being saved
# created: boolean, True if new record was created
# **kwargs: keyword arguments 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) # create profile for the user that has been created

# send a signal when a User model is being saved (updated)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
