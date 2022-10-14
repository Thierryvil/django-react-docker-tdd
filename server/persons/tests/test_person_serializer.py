from django.test import TestCase
from persons.serializers import PersonSerializer
from rest_framework.exceptions import ValidationError


class TestPersonSerializer(TestCase):
    def test_shoudnt_able_to_add_new_person_with_empty_name(self):
        data = {
            "name": "",
        }
        serializer = PersonSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
