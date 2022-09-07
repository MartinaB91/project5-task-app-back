from rest_framework import serializers
from .models import Profile
from .serializers import FamilyMemberSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    family_members = FamilyMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'created_at', 'updated_at', 'family_members')