from __future__ import unicode_literals

from django.conf import settings

from opentok import MediaModes

def create_session():
    return settings.OPENTOK_APP.create_session(media_mode=MediaModes.routed)
