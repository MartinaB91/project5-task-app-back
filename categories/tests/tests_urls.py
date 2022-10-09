import pytest
from django.urls import reverse, resolve
from categories.views import CategoryList


@pytest.mark.django_db
def test_categories_url():
    """
    Tests the categories url 
    """
    url = reverse('categories')
    assert resolve(url).func.view_class == CategoryList
