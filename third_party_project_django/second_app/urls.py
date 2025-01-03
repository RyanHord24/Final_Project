from django.urls import path
from .views import All_Pokemon
from .views import A_Pokemon

urlpatterns = [
    path('', All_Pokemon.as_view(), name="all_pokemon"),
    path('<str:id>/', A_Pokemon.as_view(), name="a_pokemon")
]