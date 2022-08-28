import pytest
from django.test import TestCase
from task.models import Task, Category
from family_member.models import FamilyMember
from datetime import date
import datetime

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        family_member = FamilyMember.objects.create(
            name = 'Emil',
            family_member_img = 'emil.PNG',
            star_points = 30,
            ongoing_tasks = 2,
            closed_tasks = 10
            )
        category = Category.objects.create(
            name = 'Test category 1',
        )
        task = Task.objects.create(
            title = 'Test task',
            creator = family_member,
            category = category,
            end_date = date.today(),
            description = 'This is a test task description',
            star_points = 0,
            assigned = family_member,
            )

    def test_task_title(self):
        """
        Tests that the task title is as expected.
        """
        task = Task.objects.first()
        assert task.title == 'Test task'

    def test_task_creator(self):
        """
        Tests that the task is created by our created family member. 
        """
        task = Task.objects.first()
        assert task.creator.name == 'Emil'
    
    def test_task_created_on(self):
        """
        Tests that the task is created on the day we expected. 
        """
        task = Task.objects.first()
        created_on_datetime = datetime.datetime(task.created_on.year, task.created_on.month, task.created_on.day)
        assert created_on_datetime.strftime('%Y-%m-%d') == date.today().strftime('%Y-%m-%d')

    def test_task_updated_on(self):
        """
        Tests that the task is updated on the day we expected. 
        """
        task = Task.objects.first()
        updated_on_datetime = datetime.datetime(task.updated_on.year, task.updated_on.month, task.updated_on.day)
        assert updated_on_datetime.strftime('%Y-%m-%d') == date.today().strftime('%Y-%m-%d')


    def test_task_description(self):
        """
        Tests that the task description is as expected.
        """
        task = Task.objects.first()
        assert task.description == 'This is a test task description'
    

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
        assert task.assigned.name == 'Emil'
    
    def test_task_category(self):
        task = Task.objects.first()
        assert task.category.name == 'Test category 1'

    
class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            name = 'Test category 2',
        )

    def test_category_name(self):
        """
        Tests that the category name is as expected
        """
        category = Category.objects.first()
        assert category.name == 'Test category 2'

    def test_category_icon_default(self):
        pass