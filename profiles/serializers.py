from rest_framework import serializers
from family_member.models import FamilyMember
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Profile
        fields = [
            "user",
            "created_at",
            "updated_at",
        ]
