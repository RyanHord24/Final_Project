from django.urls import path
from .views import All_Rentals

urlpatterns = [
    path('', All_Rentals.as_view(), name='all_rentals'),
]