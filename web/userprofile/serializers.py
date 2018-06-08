from __future__ import unicode_literals

from django.contrib.auth.models import User

from .models import Profile

from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'full_name', 'owner_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff', 'profile')
