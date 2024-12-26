from django.db import models
from user_app.models import User
from favorites.models import FavoriteCountry

class Notebook(models.Model):
    details = models.TextField()
    favorite_country = models.ForeignKey(
    FavoriteCountry, on_delete=models.CASCADE, related_name="notebooks"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notebooks")

    def __str__(self):
        return f"Notebook for {self.favorite_country} by {self.user}"
