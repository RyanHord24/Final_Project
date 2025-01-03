from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Cars 
from .serializers import CarsSerializer 
from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

class all_cars(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serialized_all_cars = CarsSerializer(cars, many=True)
        return Response(serialized_all_cars.data) 

    def post(self, request):
        new_car = CarsSerializer(data=request.data)
        if new_car.is_valid():
            new_car.save()
            return Response(new_car.data, status=HTTP_201_CREATED)
        else:
            return Response(new_car.errors, status=HTTP_400_BAD_REQUEST)

class A_Car(APIView):
     def get(self, request, id):
        car = None
        car = Cars.objects.get(make = id.title()) # <== We only accept names in Title format so lets use the `title` method to ensure we have the user input in the correct format
        return Response(CarsSerializer(car).data)

     def put(self, request, id):
        car = get_object_or_404(Cars, make=id.title())
        serialized_car = CarsSerializer(car, data = request.data, partial = True)
        if serialized_car.is_valid():
            serialized_car.save()
            return Response(status=HTTP_200_OK)
    
     def delete(self, request, id):
        car = Cars.objects.get(make = id.title())
        car.delete()
        return Response(status=HTTP_204_NO_CONTENT)
