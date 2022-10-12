import pytest
from django.urls import reverse
from django.contrib.auth.models import User
import json


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Tests profile detail view response status code 200
    """
    user = User.objects.create(username="Olle")
    url = reverse("my_profile", args=[user.profile.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_view_data(client):
    """
    Tests profile detail view response data
    """
    user = User.objects.create(username="Olle")
    url = reverse("my_profile", args=[user.profile.id])
    response = client.get(url)
    assert response.data["user"] == user.username
