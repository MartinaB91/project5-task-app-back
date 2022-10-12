import pytest
from django.test import TestCase
from task.models import Task
from family_member.models import FamilyMember
from categories.models import Category
from datetime import date
import datetime
from django.contrib.auth.models import User


class TaskModelTest(TestCase):
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

    def test_task_belongs_to_profile(self):
        """
        Tests that the task belongs to our above created profile
        """
        task = Task.objects.first()
        assert task.belongs_to_profile.user.username == "Emils-profile"

    def test_task_title(self):
        """
        Tests that the task title is as expected.
        """
        task = Task.objects.first()
        assert task.title == "Test task"

    def test_task_creator(self):
        """
        Tests that the task is created by our created family member.
        """
        task = Task.objects.first()
        assert task.creator.name == "Emil"

    def test_task_created_on(self):
        """
        Tests that the task is created on the day we expected.
        """
        task = Task.objects.first()
        created_on_datetime = datetime.datetime(
            task.created_on.year, task.created_on.month, task.created_on.day
        )
        assert created_on_datetime.strftime("%Y-%m-%d") == date.today().strftime(
            "%Y-%m-%d"
        )

    def test_task_updated_on(self):
        """
        Tests that the task is updated on the day we expected.
        """
        task = Task.objects.first()
        updated_on_datetime = datetime.datetime(
            task.updated_on.year, task.updated_on.month, task.updated_on.day
        )
        assert updated_on_datetime.strftime("%Y-%m-%d") == date.today().strftime(
            "%Y-%m-%d"
        )

    def test_task_description(self):
        """
        Tests that the task description is as expected.
        """
        task = Task.objects.first()
        assert task.description == "This is a test task description"

    def test_task_star_points(self):
        """
        Tests that the task star points is as expected.
        """
        task = Task.objects.first()
        assert task.star_points == 0

    def test_task_assigned(self):
        """
        Tests that the task is assigned to our created family member.
        """
        task = Task.objects.first()
        assert task.assigned.name == "Emil"

    def test_task_category(self):
        task = Task.objects.first()
        assert task.category.name == "Test category 1"
