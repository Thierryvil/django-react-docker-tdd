from persons.models import PersonModel
from rest_framework import serializers

from cars.models import CarModel

MAXIMUM_NUMBER_OF_CARS_PER_PERSON = 3


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("id", "color", "type", "person")

    color = serializers.ChoiceField(choices=CarModel.COLORS)
    type = serializers.ChoiceField(choices=CarModel.TYPES)
    person = serializers.IntegerField(source="person.id")

    def create(self, validated_data):
        person = PersonModel.objects.get(id=validated_data["person"]["id"])
        validated_data["person"] = person
        instance = CarModel.objects.create(**validated_data)
        return instance

    def validate_color(self, value):
        if value not in dict(CarModel.COLORS):
            raise serializers.ValidationError("Invalid Color")
        return value

    def validate_type(self, value):
        if value not in dict(CarModel.TYPES):
            raise serializers.ValidationError("Invalid Color")
        return value

    def validate_person(self, value):
        if not PersonModel.objects.filter(id=value).exists():
            raise serializers.ValidationError("Person Doesn't exist")
        if len(CarModel.objects.filter(person=value)) >= MAXIMUM_NUMBER_OF_CARS_PER_PERSON:
            raise serializers.ValidationError("Maximum Number Of Cars Achieved")
        return value
