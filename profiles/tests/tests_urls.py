import pytest
from django.urls import reverse, resolve
from profiles.views import ProfileDetailList, ProfileList
from django.contrib.auth.models import User



@pytest.mark.django_db
def test_profile_settings_url():
    """
    Tests the profile settings url 
    """
    user = User.objects.create(username = "Olle")
    url = reverse('my_profile', args=[user.profile.id])
    assert resolve(url).func.view_class ==  ProfileDetailList
