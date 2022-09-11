from rest_framework import serializers
from family_member.models import FamilyMember
from .models import Profile



class SimpleFamilyMemberSerializer(serializers.ModelSerializer):

    class Meta: 
        model = FamilyMember
        fields = (
            'name', 'belongs_to_profile',
            )

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('user', 'created_at', 'updated_at',)

