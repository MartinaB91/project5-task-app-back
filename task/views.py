from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from profiles.models import Profile
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskListView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        task = Task.objects.filter(belongs_to_profile=profile)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
  