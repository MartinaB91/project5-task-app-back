import pytest
from django.urls import reverse
from django.test import TestCase
from categories.models import Category


class CategoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            name = 'Test category 2',
        )

    @pytest.mark.django_db
    def test_category_post_list_view(self):
        """
        Tests category post list view response 
        """
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_categories_list_view_response_data(self):
        """
        Tests category list view response data
        """
        category = Category.objects.first()
        url = reverse('categories')
        response = self.client.get(url)
        print(response.data)
        assert response.data[0]['name'] == category.name