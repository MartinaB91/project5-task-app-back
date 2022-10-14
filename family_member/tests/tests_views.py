import pytest
from django.urls import reverse
from django.test import TestCase
from profiles.models import Profile
from family_member.views import FamilyMemberList, FamilyMemberDetailView
from family_member.models import FamilyMember
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
import ast

# https://www.django-rest-framework.org/api-guide/testing/


class FamilyMemberViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # factory = APIRequestFactory()
        user = User.objects.create(username="Lotta")
        familyMember = FamilyMember.objects.create(
            name="Pippi", belongs_to_profile=user.profile
        )

    @pytest.mark.django_db
    def test_FamilyMember_post_list_view(self):
        """
        Tests FamilyMember post list view response
        """
        # Arrange
        view = FamilyMemberList.as_view()
        factory = APIRequestFactory()
        user = User.objects.first()
        # Act
        request = factory.get("members/")
        force_authenticate(request, user=user)
        response = view(request)
        response.render()
        # Assert
        # https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary
        # response.content is byte type, link above is how to convert to dictionary
        response_content = response.content.decode("UTF-8")
        response_dict = ast.literal_eval(response_content)

        assert response_dict[0]["id"] == 1
        assert response_dict[0]["belongs_to_profile"] == "Lotta"
        assert response_dict[0]["closed_tasks"] == 0
        assert response_dict[0]["ongoing_tasks"] == 0
        assert response_dict[0]["star_points"] == 0


    @pytest.mark.django_db
    def test_FamilyMember_post_detail_view(self):
        """
        Tests FamilyMember post list view response
        """
        # Arrange
        view = FamilyMemberDetailView.as_view()
        factory = APIRequestFactory()
        user = User.objects.first()
        # Act
        request = factory.get("members/1")  # Is only one user therefore id = 1
        force_authenticate(request, user=user)
        response = view(request, pk=user.id)
        response.render()

        # response.content is byte type, link above is how to convert to dictionary
        response_content = response.content.decode("UTF-8")
        response_dict = ast.literal_eval(response_content)

        assert response_dict["id"] == 1
        assert response_dict["belongs_to_profile"] == "Lotta"
        assert response_dict["closed_tasks"] == 0
        assert response_dict["ongoing_tasks"] == 0
        assert response_dict["star_points"] == 0

