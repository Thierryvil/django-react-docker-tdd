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

    def test_shouldnt_be_possible_to_add_a_new_person_with_an_existing_name(self):
        data = {
            "name": "any name",
        }
        self.client.post("/persons/", data, format="json")
        response = self.client.post("/persons/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_be_able_to_add_new_person_with_valid_name(self):
        data = {
            "name": "any name",
        }
        response = self.client.post("/persons/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
