from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from persons.models import PersonModel
from persons.serializers import PersonSerializer


class PersonViews(APIView):
    def post(self, request: Request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request):
        persons = PersonModel.objects.all().values()
        return Response(persons, status=status.HTTP_200_OK)
