from rest_framework import serializers
from .models import Task
from family_member.models import FamilyMember


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    creator = serializers.StringRelatedField(source='creator.name')

    class Meta:
        model = Task
        fields = [
            'title',
            'creator',
            'category',
            'end_date',
            'description',
            'star_points',
            'assigned',
        ]