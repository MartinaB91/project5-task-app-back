import pytest
from django.test import TestCase
from family_member.models import FamilyMember
from profiles.models import Profile
from django.contrib.auth.models import User



class FamilyMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        This setup is intentionally leaving out FamilyMember role.
        This because default value is tested. 
        """
        user = User.objects.create(username= 'Pippis-profile')

        family_member = FamilyMember.objects.create(
            belongs_to_profile= user.profile,
            name = 'Pippi',
            family_member_img = 'pippi.PNG',
            star_points = 0,
            ongoing_tasks = 0,
            closed_tasks = 0
            )

    def test_family_members_name(self):
        """
        Tests that the family member is given the expected name.
        """
        family_member = FamilyMember.objects.first()
        assert family_member.name == 'Pippi'
    
    def test_family_members_img(self):
        pass 

    
    def test_family_members_role_default_value(self):
        """
        Tests that a family members role by default is 0(child).
        """
        family_member = FamilyMember.objects.first()
        assert family_member.role == 0

    def test_family_members_role(self):
        """
        Tests that you can set a value of parent to role
        """
        family_member = FamilyMember.objects.first()
        family_member.role = 1
        assert family_member.role == 1

    def test_family_members_star_points(self):
        """
        Tests that the value of star points is as expected.
        """
        family_member = FamilyMember.objects.first()
        assert family_member.star_points == 0

    def test_family_members_ongoing_tasks(self):
        """
        Tests that the value of ongoing tasks is as expected.
        """
        family_member = FamilyMember.objects.first()
        assert family_member.ongoing_tasks == 0 


    def test_family_members_closed_tasks(self):
        """
        Tests that the value of closed tasks is as expected.
        """
        family_member = FamilyMember.objects.first()
        assert family_member.closed_tasks == 0 




    