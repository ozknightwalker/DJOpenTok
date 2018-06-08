from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    owner = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    full_name =  models.CharField(max_length=255, blank=True)
