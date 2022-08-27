import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create('Pippi', 'pippi@pippi.se', 'pippispassword')
        Profile.objects.create(user=user)

    def test_user_in_profile(self):
        profile = Profile.objects.first()
        user_in_profile = profile.user
        assert user_in_profile.username == 'Pippi'