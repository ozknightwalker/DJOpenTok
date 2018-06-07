from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.test import TestCase

from userprofile.models import Profile


class CreateUserProfileTestCase(TestCase):
    """ Testcase for create_userprofile """

    def test_create_userprofile_on_create(self):
        user = User.objects.create_user(username='test', password='test')
        self.assertIsNotNone(user.profile)
