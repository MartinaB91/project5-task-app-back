import pytest
from django.test import TestCase
from categories.models import Category


class CategoryModelTest(TestCase):
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