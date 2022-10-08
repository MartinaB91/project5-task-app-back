from rest_framework import serializers
from .models import FamilyMember
from profiles.models import Profile

# from django.contrib.auth.decorators import login_required

# @login_required
class FamilyMemberSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(source='belongs_to_profile.user.username')
    name = serializers.CharField(max_length=200)
    # family_member_img = serializers.ReadOnlyField(source='family_member_img.url') 
    role = serializers.ChoiceField(choices=FamilyMember.ROLE_PRIVILEGE)


    class Meta: 
        model = FamilyMember
        fields = [
            'id',
            'belongs_to_profile',
            'name',
            'family_member_img',
            'role',
            'star_points',
            'ongoing_tasks',
            'closed_tasks',
        ]
