from __future__ import unicode_literals

from .viewsets import UserViewSet

from djopentok.routers import router

router.register(r'users', UserViewSet)
