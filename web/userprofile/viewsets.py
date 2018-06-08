from __future__ import unicode_literals

from django.contrib.auth.models import User

from .serializers import UserSerializer

from rest_framework import permissions, viewsets


class UserViewSet( viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)
