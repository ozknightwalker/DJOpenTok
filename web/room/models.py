from __future__ import unicode_literals

from django.db import models

from djopentok.utils.opentok import create_session


class Room(models.Model):
    session_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.session_id = create_session().session_id
        return super().save(*args, **kwargs)
