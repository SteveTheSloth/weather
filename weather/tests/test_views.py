
import pytest
from weather.utils import create_records
from django.urls import reverse

@pytest.mark.django_db
def test_index_view_get(client):
   url = reverse("index")
   response = client.get(url)
   assert response.status_code == 200
   
@pytest.mark.django_db
def test_index_view_post(client):
   create_records(3333231, "standard", "")
   url = reverse("index")
   response = client.post(url, data={"choice": "3333231 standard"})
   assert response.status_code == 302
   
@pytest.mark.django_db
def test_index_view_post_two(client):
   create_records(3333231, "standard", "")
   url = reverse("index")
   response = client.post(url, data={"city": "Glasgow", "country": "GB", "units": "metric"})
   assert response.status_code == 302
   
@pytest.mark.django_db
def test_detail_view_one(client):
   create_records(3333231, "standard", "")
   url = reverse("detail", args=[3333231])
   response = client.get(url)
   assert response.status_code == 200
   