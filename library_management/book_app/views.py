from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response

class All_Books(APIView):
    pass