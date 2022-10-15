from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class TestPersonView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_shoudnt_be_able_to_add_new_person_with_empty_name(self):
        data = {
            "name": "",
        }
        response = self.client.post("/persons/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)