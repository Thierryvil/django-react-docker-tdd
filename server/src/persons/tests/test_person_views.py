from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class TestPersonView(APIClient):
    def setUp(self) -> None:
        self.client.post("/persons/", {"name": "already-name"}, format="json")
        self.user = User.objects.create(username="testing", password="testing123")
        self.token = RefreshToken.for_user(self.user)

    def test_shoudnt_be_able_to_add_new_person_with_empty_name_with_status_code_400(self):
        data = {
            "name": "",
        }
        self.client.credentials
        response = self.client.post("/persons/", data, format="json", HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_shouldnt_be_possible_to_add_a_new_person_with_an_existing_name_with_status_code_400(self):
        data = {
            "name": "already-name",
        }
        response = self.client.post("/persons/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_be_able_to_add_new_person_with_valid_name_with_status_code_201(self):
        data = {
            "name": "any name",
        }
        response = self.client.post("/persons/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_be_possible_to_return_all_existing_person_with_status_code_200(self):
        response = self.client.get("/persons/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{"id": 1, "name": "already-name"}])
