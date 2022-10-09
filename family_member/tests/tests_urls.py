import pytest
from django.urls import reverse, resolve
from family_member.views import FamilyMemberList, FamilyMemberDetailList
from django.contrib.auth.models import User


        
def test_family_member_list_url():
    """
    Tests the family member list url 
    """
    url = reverse('family_member_list')
    assert resolve(url).func.view_class == FamilyMemberList

@pytest.mark.django_db
def test_family_member_detail_url():
    """
    Tests the family member detail url 
    """
    user = User.objects.create(username= 'Anna')
    url = reverse('family_member_detail', args=[user.id])
    assert resolve(url).func.view_class == FamilyMemberDetailList