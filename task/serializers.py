from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(source='belongs_to_profile.user.username')
    category_name = serializers.CharField(source='category.name')
    category = serializers.StringRelatedField(source='category.id')

    class Meta:
        model = Task
        fields = [
            'id',
            'belongs_to_profile',
            'title',
            'creator',
            'category',
            'category_name',
            'end_date',
            'description',
            'star_points',
            'assigned',
        ]