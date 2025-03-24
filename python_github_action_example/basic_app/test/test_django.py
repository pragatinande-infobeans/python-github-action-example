import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_django_running(client):
    response = client.get("/")
    print(response.content)  # Print response content
    assert response.status_code == 200