from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Task
from profiles.models import Profile
from categories.models import Category
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.http import Http404
from family_star.permissions import IsOwner
from family_member.models import FamilyMember
from categories.models import Category


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
            validated_data = serializer.validated_data
            profile = Profile.objects.get(user=request.user)
            request_category = Category.objects.get(name=validated_data.get('category')['name'])

            serializer.save(belongs_to_profile=profile, category=request_category)
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

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return  Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
class AssignTask(APIView):
    serialzer_class = TaskSerializer
    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404
    
    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, instance, validated_data):
    #     """
    #     Used for updating task form
    #     """
    #     task = Task.objects.get(id=instance.id)

    #     if validated_data.get('title') is not None:
    #         task.title = validated_data.get('title')
    #         task.category = Category.objects.get(name=validated_data.get('category')['name'])
    #         task.end_date = validated_data.get('end_date')
    #         task.description = validated_data.get('description')
    #         task.star_points = validated_data.get('star_points')
    #         if (validated_data.get('assigned') is not None):
    #             task.assigned = FamilyMember.objects.get(name=validated_data.get('assigned'))
    #     if validated_data.get('title') is None:
    #         task.assigned = validated_data.get('assigned')
    #         familyMember = FamilyMember.objects.get(name=validated_data.get('assigned'))
    #         familyMember.ongoing_tasks = familyMember.ongoing_tasks + 1  # Check if replace with objects filter .count()
    #         familyMember.save()

    #     task.save()
    #     return task
