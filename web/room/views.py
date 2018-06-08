from __future__ import unicode_literals

from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'room/homepage.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['with_banner'] = True
        return context


class LiveMixins(object):
    user_type = None

    def get_context_data(self):
        context = super().get_context_data()
        context['user_type'] = self.user_type
        return context


class HostView(LiveMixins, TemplateView):
    template_name = 'room/live/host.html'
    user_type = 'host'


class ParticipantView(LiveMixins, TemplateView):
    template_name = 'room/live/participant.html'
    user_type = 'participant'
