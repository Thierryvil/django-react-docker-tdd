from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from persons.serializers import PersonSerializer


@api_view(["POST"])
def add_new_person(request: Request):
    data = request.data
    serializer = PersonSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
