from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(source='belongs_to_profile.user.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'belongs_to_profile',
            'title',
            'creator',
            'category',
            'end_date',
            'description',
            'star_points',
            'assigned',
        ]