from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(owner=instance, full_name=instance.get_full_name())
