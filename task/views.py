from django.shortcuts import render
from rest_framework import generics, filters, status, permissions
from rest_framework.views import APIView
from rest_framework.mixins import UpdateModelMixin
from .models import Task
from profiles.models import Profile
from categories.models import Category
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.http import Http404
from family_star.permissions import IsOwner
from family_member.models import FamilyMember
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from family_star.permissions import IsOwner


class TaskListView(generics.ListCreateAPIView):
    """
    Used for view all tasks that belongs to
    current profile and for creating a new task.
    """

    permission_classes = [IsOwner]
    serialzer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
    ]
    queryset = Task.objects.all()

    def get_serializer_class(self):
        return TaskSerializer

    def get(self, request):
        """
        Get all tasks that belongs to a profile or get the results of from search query or filtering.
        """
        profile = Profile.objects.get(user=request.user)
        family_members = FamilyMember.objects.filter(belongs_to_profile=profile)
        if (
            "&search" in request.get_full_path()
            and "?filter" in request.get_full_path()
        ):  # Get searching or filtering
            search = self.request.query_params.get("search")
            filter = self.request.query_params.get("filter")
            if filter == "my_tasks":
                current_family_member_id = self.request.query_params.get(
                    "family_member_id"
                )
                task = Task.objects.filter(
                    belongs_to_profile=profile,
                    assigned_id=current_family_member_id,
                    status="Todo",
                ).order_by("end_date")
            elif filter == "assigned":
                task = Task.objects.filter(
                    ~Q(assigned=None), belongs_to_profile=profile, status="Todo"
                ).order_by("end_date")
            elif filter == "done":
                task = Task.objects.filter(
                    belongs_to_profile=profile, status="Done"
                ).order_by("-end_date")
            elif filter == "all_tasks":
                task = Task.objects.filter(belongs_to_profile=profile).order_by(
                    "-end_date"
                )
            else:
                task = Task.objects.filter(
                    Q(assigned=None), belongs_to_profile=profile, status="Todo"
                ).order_by("end_date")
            if search != "undefined":  # Search in already filtered tasks
                task = task.filter(
                    Q(belongs_to_profile=profile) & Q(title__icontains=search)
                    | Q(description__icontains=search)
                ).order_by("created_on")
        else:  # Get without search or filter. Default value for taskboard tasks (show tasks not assigned that has status todo).
            task = Task.objects.filter(
                Q(assigned=None), belongs_to_profile=profile, status="Todo"
            ).order_by("end_date")
        serializer = TaskSerializer(task, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            profile = Profile.objects.get(user=request.user)
            request_category = Category.objects.get(
                name=validated_data.get("category")["name"]
            )

            serializer.save(belongs_to_profile=profile, category=request_category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Used for displaying one task that belongs to
    the current profile, update and delete a task.
    """

    permission_classes = [IsOwner]
    serialzer_class = TaskSerializer

    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            if self.request.user == task.belongs_to_profile:
                self.check_object_permissions(self.request, task)
                return task
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        if request.user.is_authenticated:
            task = Task.objects.get(id=pk)
            profile = Profile.objects.get(id=self.request.user.profile.id)
            if profile == task.belongs_to_profile:
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class TaskDone(APIView, UpdateModelMixin):
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
