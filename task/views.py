from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Task
from profiles.models import Profile
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskListView(APIView):
    """
    Views all tasks that belongs to current profile. 
    """
    serialzer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        task = Task.objects.filter(belongs_to_profile=profile)
        serializer = TaskSerializer(task, many=True, context={'request': request}
        )
        return Response(serializer.data)
  
    def post(self, request):
        serializer = TaskSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            profile = Profile.objects.get(user=request.user)
            serializer.save(belongs_to_profile=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)