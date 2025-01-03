from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student # specify what model this serializer is for
        fields = ['id', 'name', 'student_email', 'personal_email', 'dorm_number']