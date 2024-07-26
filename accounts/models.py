from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role_choices = [
        (0,'Admin'),
        (1, 'Staff'),
        (2, 'Student'),
    ]
  #  user_type=models.CharField(choices=role_choices,max_length=50,blank=True,null=True)
    role = models.SmallIntegerField(choices=role_choices,null=True,blank=True)
    is_verified = models.BooleanField(default=False)


  
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

