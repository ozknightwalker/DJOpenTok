from __future__ import unicode_literals

from django.conf import settings
from django.views.generic import TemplateView

from djopentok.utils.opentok import generate_token

from .models import Room

class HomepageView(TemplateView):
    template_name = 'room/homepage.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['with_banner'] = True
        return context


class OpenTokMixin(object):

    def get_context_data(self):
        context = super().get_context_data()
        room = Room.objects.first()
        context['OPENTOK'] = dict(
            session_id=room.session_id,
            api_key=settings.OPENTOK_API_KEY,
            token=generate_token(room.session_id)
        )
        return context


class LiveMixins(object):
    user_type = None

    def get_context_data(self):
        context = super().get_context_data()
        context['user_type'] = self.user_type
        return context


class HostView(OpenTokMixin, LiveMixins, TemplateView):
    template_name = 'room/room.html'
    user_type = 'host'


class ParticipantView(LiveMixins, TemplateView):
    template_name = 'room/room.html'
    user_type = 'participant'
