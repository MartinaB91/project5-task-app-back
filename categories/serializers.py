from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    icon = serializers.ReadOnlyField(source="icon.url")

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "icon",
        ]
