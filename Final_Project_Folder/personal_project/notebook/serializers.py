from rest_framework import serializers
from .models import Notebook
from favorites.serializers import FavoriteCountrySerializer

class NotebookSerializer(serializers.ModelSerializer):

    favorite_country = FavoriteCountrySerializer(read_only=True)

    class Meta:
        model = Notebook
        fields = ['id', 'details', 'favorite_country', 'user']
