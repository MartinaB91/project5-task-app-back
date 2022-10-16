import pytest
from django.urls import reverse
from django.test import TestCase
from task.models import Task
from categories.models import Category
from family_member.models import FamilyMember
from django.contrib.auth.models import User
from task.views import TaskListView, TaskDetail
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
import ast
from datetime import date
import datetime
import json


class TaskViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="Lotta")
        family_member = FamilyMember.objects.create(
            name="Pippi", belongs_to_profile=user.profile
        )
        category = Category.objects.create(
            name="Test category 2",
        )
        task = Task.objects.create(
            belongs_to_profile_id=user.profile.id,
            title="Test task 2",
            creator=family_member,
            category=category,
            end_date=date.today(),
            description="This is a test task description 2",
            star_points=0,
            status="Todo",
        )

    @pytest.mark.django_db
    def test__todo_filter_task_post_list_view(self):
        """
        Tests default(todo) task post list view response
        """
        view = TaskListView.as_view()
        factory = APIRequestFactory()
        request = factory.get("tasks/")
        task = Task.objects.first()
        force_authenticate(request, user=User.objects.first()) # Sign in
        response = view(request)
        response.render()
        # Parse json string to object
        # https://reqbin.com/code/python/g4nr6w3u/python-parse-json-example
        data = json.loads(response.content)

        assert data[0]["id"] == 1
        assert data[0]["belongs_to_profile"] == "Lotta"
        assert data[0]["title"] == "Test task 2"
        assert data[0]["creator"] == 1
        assert data[0]["category"] == '1'
        assert data[0]["description"] == "This is a test task description 2"
        assert data[0]["star_points"] == 0
        assert data[0]["status"] == "Todo"


