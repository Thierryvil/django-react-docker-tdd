from rest_framework import serializers

from persons.models import PersonModel


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = "__all__"

    name = serializers.CharField()

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Empty Name")
