import pytest
from django.urls import reverse, resolve
from django.test import TestCase
from task.views import TaskListView, TaskDetail, AssignTask, TaskDone
from django.contrib.auth.models import User
from family_member.models import FamilyMember
from categories.models import Category
from task.models import Task
from datetime import date
import datetime


class TaskUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Emils-profile")
        family_member = FamilyMember.objects.create(
            belongs_to_profile=user.profile,
            name="Emil",
            family_member_img="emil.PNG",
            star_points=30,
            ongoing_tasks=2,
            closed_tasks=10,
        )
        category = Category.objects.create(
            name="Test category 1",
        )
        task = Task.objects.create(
            belongs_to_profile_id=user.profile.id,
            title="Test task",
            creator=family_member,
            category=category,
            end_date=date.today(),
            description="This is a test task description",
            star_points=0,
            assigned=family_member,
        )

    def test_task_list_view_url(self):
        """
        Tests the task list view url
        """
        url = reverse("task_list")
        assert resolve(url).func.view_class == TaskListView

    @pytest.mark.django_db
    def test_task_detail_view_url(self):
        """
        Tests the task detail view url
        """
        task = Task.objects.first()
        url = reverse("task", args=[task.id])
        assert resolve(url).func.view_class == TaskDetail

    @pytest.mark.django_db
    def test_task_assign_view_url(self):
        """
        Tests the task assign view url
        """
        task = Task.objects.first()
        url = reverse("task_assigned", args=[task.id])
        assert resolve(url).func.view_class == AssignTask

    @pytest.mark.django_db
    def test_task_done_view_url(self):
        """
        Tests the task done view url
        """
        task = Task.objects.first()
        url = reverse("task_done", args=[task.id])
        assert resolve(url).func.view_class == TaskDone
