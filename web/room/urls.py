from __future__ import unicode_literals

from django.urls import path

from .views import HomepageView, HostView, ParticipantView

urlpatterns = [
    path('', HomepageView.as_view()),
    path('host/', HostView.as_view()),
    path('participant/', ParticipantView.as_view()),
]
