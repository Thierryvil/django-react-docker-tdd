from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import CarModel
from cars.serializers import CarSerializer


class CarView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        data = request.data
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request):
        cars = CarModel.objects.all().values()
        return Response(cars, status=status.HTTP_200_OK)
