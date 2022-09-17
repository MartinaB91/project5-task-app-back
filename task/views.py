from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Task
from profiles.models import Profile
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.http import Http404
from family_star.permissions import IsOwner


class TaskListView(APIView):
    """
    Used for view all tasks that belongs to 
    current profile and for creating a new task.
    """
    serialzer_class = TaskSerializer

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

class TaskDetail(APIView):
    """
    Used for displaying one task that belongs to 
    the current profile, update and delete a task. 
    """
    serialzer_class = TaskSerializer
    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    