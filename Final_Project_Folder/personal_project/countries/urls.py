from django.urls import path
from .views import Get_country

urlpatterns = [
    path('<str:id>/', Get_country, name='get_country'),
]
