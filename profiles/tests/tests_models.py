import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from datetime import date
import datetime


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('Pippi') # Creates a user with only a username

    def test_profile_user_username(self):
        """
        Tests that Profile model user is the same as created users username.
        """
        profile = Profile.objects.first()
        user_in_profile = profile.user
        assert user_in_profile.username == 'Pippi'
    
    def test_profile_user_created_at(self):
        """
        Tests that the created at date is correct.
    
        """
        profile = Profile.objects.first()
        created_at_datetime = datetime.datetime(profile.created_at.year, profile.created_at.month, profile.created_at.day)
        assert created_at_datetime.strftime('%Y-%m-%d') == date.today().strftime('%Y-%m-%d')

    def test_profile_user_updated_at(self):
        """
        Tests that the updated at date is correct.
    
        """
        profile = Profile.objects.first()
        updated_at_datetime = datetime.datetime(profile.updated_at.year, profile.updated_at.month, profile.updated_at.day)
        assert updated_at_datetime.strftime('%Y-%m-%d') == date.today().strftime('%Y-%m-%d')