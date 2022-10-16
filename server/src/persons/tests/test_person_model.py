from django.test import TestCase
from persons.models import PersonModel


class TestPersonModel(TestCase):
    def test_should_be_able_to_create_a_new_person(self):
        person = PersonModel.objects.create(name="any name")
        self.assertEqual(person.name, "any name")
