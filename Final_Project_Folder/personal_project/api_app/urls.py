from django.urls import path
from . import views

urlpatterns = [
    path('country/<str:country_name>/', views.CountryDetailView.as_view(), name='country_detail'),
]
