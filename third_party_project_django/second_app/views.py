from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pokemon 
from .serializers import PokemonSerializer 
from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

class All_Pokemon(APIView):
    def get(self, request):
        all_pokemon = Pokemon.objects.all()
        serialized_all_pokemon = PokemonSerializer(all_pokemon, many=True)
        return Response(serialized_all_pokemon.data)

class A_Pokemon(APIView):
     def get(self, request, id):
        a_pokemon = None
        a_pokemon = Pokemon.objects.get(name = id.title()) # <== We only accept names in Title format so lets use the `title` method to ensure we have the user input in the correct format
        return Response(PokemonSerializer(a_pokemon).data)