from django.contrib import admin
from countries.models import Country 
from favorites.models import FavoriteList, FavoriteCountry 
from notebook.models import Notebook

admin.site.register(FavoriteList)
admin.site.register(FavoriteCountry)
admin.site.register(Country)
admin.site.register(Notebook)