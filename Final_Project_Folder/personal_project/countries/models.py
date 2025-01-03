from django.db import models

class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
