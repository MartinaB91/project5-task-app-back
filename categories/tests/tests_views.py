import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_category_post_list_view(client):
    """
    Tests category post list view response 
    """
    url = reverse('categories')
    response = client.get(url)
    assert response.status_code == 200
