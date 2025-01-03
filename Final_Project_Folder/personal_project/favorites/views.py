from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import FavoriteList
from .models import FavoriteCountry
from countries.models import Country
from user_app.models import User
from .serializers import FavoriteListSerializer, FavoriteCountrySerializer
from rest_framework.permissions import IsAuthenticated

class FavoriteCountryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        favorites_list, created = FavoriteList.objects.get_or_create(user=user)
        favorite_countries = FavoriteCountry.objects.filter(favorite_list=favorites_list)

        serializer = FavoriteCountrySerializer(favorite_countries, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
class FavoriteCountryView(APIView):

    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        favorites_list, created = FavoriteList.objects.get_or_create(user=user)
        country_id = request.data.get('country_id')
        
        country = get_object_or_404(Country, id=country_id)
        if FavoriteCountry.objects.filter(favorite_list=favorites_list, country=country).exists():
            return Response({"error": "Country already in favorites list."}, status=HTTP_400_BAD_REQUEST)

        favorite_country = FavoriteCountry.objects.create(favorite_list=favorites_list, country=country, travel_start_date=request.data.get('travel_start_date'), travel_end_date=request.data.get('travel_end_date'))
        serializer = FavoriteCountrySerializer(favorite_country)
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    def put(self, request, country_id):
        user = request.user
        favorite_country = FavoriteCountry.objects.get(
                favorite_list__user=user, country__id=country_id
            )
        travel_start_date = request.data.get('travel_start_date')
        travel_end_date = request.data.get('travel_end_date')

        if travel_start_date:
            favorite_country.travel_start_date = travel_start_date
        if travel_end_date:
            favorite_country.travel_end_date = travel_end_date

        favorite_country.save()

        serializer = FavoriteCountrySerializer(favorite_country)
        return Response(serializer.data, status=HTTP_200_OK)

    def delete(self, request, country_id):
        try:
            user = request.user
            favorite_country = FavoriteCountry.objects.get(
                favorite_list__user=user, country__id=country_id
            )
            favorite_country.delete()
            return Response({"message": "Favorite country deleted successfully."}, status=HTTP_200_OK)
        except FavoriteCountry.DoesNotExist:
            return Response({"error": "Favorite country not found."}, status=HTTP_404_NOT_FOUND)