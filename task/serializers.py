from rest_framework import serializers
from categories.models import Category
from family_member.models import FamilyMember
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(source='belongs_to_profile.user.username')
    category_name = serializers.CharField(source='category.name')
    category = serializers.StringRelatedField(source='category.id')
    id = serializers.IntegerField()
    
    # Inspiration from:
    # https://stackoverflow.com/questions/62847000/write-an-explicit-update-method-for-serializer
    def update(self, instance, validated_data):
        """
        Used for updating task form
        """
        task = Task.objects.get(id=validated_data.get('id'))
        task.title = validated_data.get('title')
        task.category = Category.objects.get(name=validated_data.get('category')['name'])
        task.end_date = validated_data.get('end_date')
        task.description = validated_data.get('description')
        task.star_points = validated_data.get('star_points')
        task.assigned = FamilyMember.objects.get(name=validated_data.get('assigned'))

        task.save()
        return task

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