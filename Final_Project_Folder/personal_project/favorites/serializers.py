from rest_framework import serializers
from .models import FavoriteList, FavoriteCountry
from countries.models import Country
from countries.serializers import CountrySerializer

class FavoriteCountrySerializer(serializers.ModelSerializer):
    country_id = serializers.CharField(source='country.id', read_only=True)
    country = CountrySerializer() 

    class Meta:
        model = FavoriteCountry
        fields = ['id', 'country', 'country_id', 'travel_start_date', 'travel_end_date']

class FavoriteListSerializer(serializers.ModelSerializer):
    favorite_countries = FavoriteCountrySerializer(many=True, read_only=True)

    class Meta:
        model = FavoriteList
        fields = ['id', 'user', 'favorite_countries']
