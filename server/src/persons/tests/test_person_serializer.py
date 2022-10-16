from django.test import TestCase
from persons.serializers import PersonSerializer
from rest_framework.exceptions import ValidationError


class TestPersonSerializer(TestCase):
    def test_shoudnt_be_able_to_add_new_person_with_empty_name(self):
        data = {
            "name": "",
        }
        serializer = PersonSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_shouldnt_be_possible_to_add_a_new_person_with_an_existing_name(self):
        data = {
            "name": "any name",
        }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        with self.assertRaises(ValidationError):
            serializer = PersonSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    def test_should_be_able_to_add_new_person_with_valid_name(self):
        data = {
            "name": "any name",
            "cars": [],
        }
        serializer = PersonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data["name"], "any name")
