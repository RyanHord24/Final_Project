from django.urls import path
from .views import FavoriteCountryListView, FavoriteCountryView

urlpatterns = [
    path('', FavoriteCountryListView.as_view(), name='favorite_list'),
    path('country/', FavoriteCountryView.as_view(), name='add_favorite_country'),
    path('country/<str:country_id>/', FavoriteCountryView.as_view(), name='edit_favorite_country'),
]
