from django.urls import path
from .views import All_Clients

urlpatterns = [
    path('', All_Clients.as_view(), name='all_clients'),
]