from cars.models import CarModel
from rest_framework import status
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from persons.models import PersonModel
from persons.serializers import PersonSerializer

MINIMUM_NUMER_OF_CARS_FOR_SALE_OPPORTUNITY = 0


class PersonViews(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        serializer = PersonSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request: Request):
        persons = PersonModel.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_persons_with_sales_opportunity(request: Request):
    sales_opportunity = {}
    persons = PersonModel.objects.all()
    for person in persons:
        cars = CarModel.objects.filter(person=person.id)
        if len(cars) <= MINIMUM_NUMER_OF_CARS_FOR_SALE_OPPORTUNITY:
            serialzier = PersonSerializer(person)
            sales_opportunity.setdefault(person.name, serialzier.data)
    return Response(sales_opportunity)
