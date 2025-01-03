from django.db import models
from user_app.models import User
from countries.models import Country

class FavoriteList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite_list")

    def __str__(self):
        return f"{self.user.username}'s Favorite List"

class FavoriteCountry(models.Model):
    id = models.AutoField(primary_key=True)
    favorite_list = models.ForeignKey(FavoriteList, on_delete=models.CASCADE, related_name="favorite_countries")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="favorited_by")
    travel_start_date = models.DateField(null=True, blank=True)
    travel_end_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("favorite_list", "country")

    def __str__(self):
        return f"{self.favorite_list.user.username} - {self.country.name}"
