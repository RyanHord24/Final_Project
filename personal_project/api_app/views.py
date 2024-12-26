import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CountryDetailView(APIView):
    
    def get(self, request, country_name):
        geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={country_name}&key={settings.GOOGLE_PLACES_API_KEY}'
        geocode_response = requests.get(geocode_url)
        
        if geocode_response.status_code == 200:
            geocode_data = geocode_response.json()
            
            if geocode_data['results']:
                lat = geocode_data['results'][0]['geometry']['location']['lat']
                lng = geocode_data['results'][0]['geometry']['location']['lng']
                
                places_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=50000&type=point_of_interest&key={settings.GOOGLE_PLACES_API_KEY}'
                places_response = requests.get(places_url)
                
                if places_response.status_code == 200:
                    places_data = places_response.json()
                    
                    google_photo_base_url = "https://maps.googleapis.com/maps/api/place/photo"
                    for place in places_data.get('results', []):
                        if "photos" in place:
                            photo_reference = place["photos"][0]["photo_reference"]
                            place["photo_url"] = (
                                f"{google_photo_base_url}?maxwidth=400&photoreference={photo_reference}&key={settings.GOOGLE_PLACES_API_KEY}"
                            )
                        else:
                            place["photo_url"] = None
                    
                    return Response(places_data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Unable to fetch data from Google Places API."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "No results found for the country."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Unable to fetch data from Google Geocoding API."}, status=status.HTTP_400_BAD_REQUEST)
