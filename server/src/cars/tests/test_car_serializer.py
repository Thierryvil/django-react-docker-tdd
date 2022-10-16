from cars.serializers import MAXIMUM_NUMBER_OF_CARS_PER_PERSON, CarSerializer
from django.test import TestCase
from persons.serializers import PersonSerializer
from rest_framework.exceptions import ValidationError


class TestCarSerializer(TestCase):
    def setUp(self) -> None:
        self.person = PersonSerializer().create(validated_data={"name": "any name"})

    def test_shoudnt_able_to_add_new_car_with_invalid_color(self):
        data = {
            "color": "blue",
            "type": 1,
            "person": self.person.id,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shoudnt_able_to_add_new_car_without_color(self):
        data = {
            "type": 1,
            "person": self.person.id,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shoudnt_able_to_add_new_car_with_invalid_type(self):
        data = {
            "color": 1,
            "type": 99,
            "person": self.person.id,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shoudnt_able_to_add_new_car_without_type(self):
        data = {
            "color": 1,
            "person": self.person.id,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shoudnt_able_to_add_new_car_with_invalid_person(self):
        data = {
            "color": 1,
            "type": 1,
            "person": 99,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shoudnt_able_to_add_new_car_without_person(self):
        data = {
            "color": 1,
            "type": 1,
            "person": 99,
        }
        serializer = CarSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_shouldnt_be_possible_to_add_a_new_car_when_it_has_reached_the_allowed_limit(self):
        data = {
            "color": 1,
            "type": 1,
            "person": self.person.id,
        }
        with self.assertRaises(ValidationError):
            for _ in range(0, MAXIMUM_NUMBER_OF_CARS_PER_PERSON + 1):
                serializer = CarSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

    def test_should_be_possible_to_add_a_new_car_with_valid_data(self):
        data = {
            "color": 1,
            "type": 1,
            "person": self.person.id,
        }
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
