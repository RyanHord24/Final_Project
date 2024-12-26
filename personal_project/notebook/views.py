from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .models import Notebook
from favorites.models import FavoriteCountry
from .serializers import NotebookSerializer

class NotebookView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    def get(self, request):
        user = request.user
        notebooks = Notebook.objects.filter(user=user)
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data)

    def post(self, request):
        country_id = request.data.get('country_id')
        
        if not country_id:
            return Response({"detail": "Country ID is required."}, status=HTTP_400_BAD_REQUEST)
        
        try:
            favorite_country = FavoriteCountry.objects.get(country__id=country_id)
            notebook = Notebook.objects.create(favorite_country=favorite_country, user=request.user, details="")
            return Response({"message": "Notebook created successfully", "notebook_id": notebook.id}, status=HTTP_201_CREATED)
        except FavoriteCountry.DoesNotExist:
            return Response({"detail": "Favorite country not found."}, status=HTTP_400_BAD_REQUEST)

    def put(self, request, country_id):
        user = request.user

        favorite_country = get_object_or_404(
            FavoriteCountry, country__id=country_id, favorite_list__user=user
        )

        notebook = get_object_or_404(Notebook, favorite_country=favorite_country, user=user)

        serializer = NotebookSerializer(notebook, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class NotebookDetailView(APIView):
    def delete(self, request, country_id):
        user = request.user

        favorite_country = get_object_or_404(
            FavoriteCountry, country__id=country_id, favorite_list__user=user
        )

        notebook = get_object_or_404(Notebook, favorite_country=favorite_country, user=user)

        notebook.delete()
        return Response({"message": "Notebook deleted successfully."}, status=HTTP_204_NO_CONTENT)
