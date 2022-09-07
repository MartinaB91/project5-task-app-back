from rest_framework import serializers
from .models import FamilyMember


class FamilyMember(serializers.ModelSerializer):


    class Meta: 
        model = FamilyMember
        fields = (
            'name',
            'family_member_img',
            'role',
            'star_points',
            'ongoing_tasks',
            'closed_tasks',
            )