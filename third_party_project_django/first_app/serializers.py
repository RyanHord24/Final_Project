from rest_framework import serializers # import serializers from DRF
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars # specify what model this serializer is for
        fields = ['make', 'model', 'description', 'passengers']