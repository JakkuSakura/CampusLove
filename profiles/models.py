from django.db import models
from users.models import User
from django.db.models.signals import post_save

from utils.profile_permissions import create_permissions


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16, default='', blank=True)
    sex = models.CharField(max_length=5, choices=(("male", "男"), ("female", "女")), default="female")
    phone = models.CharField(max_length=16, default='', blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        permissions = create_permissions(['view', 'send_msg'])


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)
